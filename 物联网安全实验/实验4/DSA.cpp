#include <iostream>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;

// SHA1算法实现
typedef unsigned char BYTE;
typedef unsigned int WORD;

const int BLOCK_SIZE = 64;

// circular left shift operator
#define LEFTROTATE(x, c) (((x) << (c)) | ((x) >> (32 - (c))))

void sha1(const BYTE* data, size_t len, BYTE* hash)
{
    // initialize hash values
    WORD h0 = 0x67452301;
    WORD h1 = 0xEFCDAB89;
    WORD h2 = 0x98BADCFE;
    WORD h3 = 0x10325476;
    WORD h4 = 0xC3D2E1F0;

    // pre-processing
    uint64_t total_len = len * 8;
    BYTE* padded_data = new BYTE[(len / BLOCK_SIZE + 1) * BLOCK_SIZE];
    memcpy(padded_data, data, len);
    padded_data[len] = 0x80;  // append a single '1' bit
    for (size_t i = len + 1; i < (len / BLOCK_SIZE + 1) * BLOCK_SIZE; i++)
    {
        padded_data[i] = 0x00;  // append multiple '0' bits
    }
    if (len % BLOCK_SIZE >= 56)
    {
        // append 64 bits of length info at the end of last block
        WORD* p = (WORD*)(padded_data + (len / BLOCK_SIZE + 1) * BLOCK_SIZE - 8);
        *p++ = 0;
        *p = (WORD)total_len;
        sha1(padded_data, (len / BLOCK_SIZE + 1) * BLOCK_SIZE, hash);
    }
    else
    {
        // append 64 bits of length info at the end of this block
        WORD* p = (WORD*)(padded_data + (len / BLOCK_SIZE) * BLOCK_SIZE + 56);
        *p++ = 0;
        *p = (WORD)total_len;
    }

    // process each block
    for (size_t i = 0; i < (len / BLOCK_SIZE + 1) * BLOCK_SIZE; i += BLOCK_SIZE)
    {
        WORD w[80];
        for (int j = 0; j < 16; j++)
        {
            w[j] = (padded_data[i + j * 4] << 24) |
                (padded_data[i + j * 4 + 1] << 16) |
                (padded_data[i + j * 4 + 2] << 8) |
                (padded_data[i + j * 4 + 3]);
        }
        for (int j = 16; j < 80; j++)
        {
            w[j] = LEFTROTATE(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1);
        }

        WORD a = h0;
        WORD b = h1;
        WORD c = h2;
        WORD d = h3;
        WORD e = h4;

        for (int j = 0; j < 80; j++)
        {
            WORD f, k;
            if (j < 20)
            {
                f = (b & c) | ((~b) & d);
                k = 0x5A827999;
            }
            else if (j < 40)
            {
                f = b ^ c ^ d;

                k = 0x6ED9EBA1;
            }
            else if (j < 60)
            {
                f = (b & c) | (b & d) | (c & d);
                k = 0x8F1BBCDC;
            }
            else
            {
                f = b ^ c ^ d;
                k = 0xCA62C1D6;
            }

            WORD temp = LEFTROTATE(a, 5) + f + e + k + w[j];
            e = d;
            d = c;
            c = LEFTROTATE(b, 30);
            b = a;
            a = temp;
        }

        h0 += a;
        h1 += b;
        h2 += c;
        h3 += d;
        h4 += e;
    }

    delete[] padded_data;

    // concatenate hash values
    BYTE* p = hash;
    *p++ = (h0 >> 24) & 0xFF;
    *p++ = (h0 >> 16) & 0xFF;
    *p++ = (h0 >> 8) & 0xFF;
    *p++ = h0 & 0xFF;
    *p++ = (h1 >> 24) & 0xFF;
    *p++ = (h1 >> 16) & 0xFF;
    *p++ = (h1 >> 8) & 0xFF;
    *p++ = h1 & 0xFF;
    *p++ = (h2 >> 24) & 0xFF;
    *p++ = (h2 >> 16) & 0xFF;
    *p++ = (h2 >> 8) & 0xFF;
    *p++ = h2 & 0xFF;
    *p++ = (h3 >> 24) & 0xFF;
    *p++ = (h3 >> 16) & 0xFF;
    *p++ = (h3 >> 8) & 0xFF;
    *p++ = h3 & 0xFF;
    *p++ = (h4 >> 24) & 0xFF;
    *p++ = (h4 >> 16) & 0xFF;
    *p++ = (h4 >> 8) & 0xFF;
    *p++ = h4 & 0xFF;
}

void generate_dsa_params(unsigned int p[8], unsigned int q[2], unsigned int h[8], unsigned int x[8], unsigned int y[8], unsigned int g[8])
{
    srand(time(NULL));

    // 生成随机数k
    unsigned int k[8];
    for (int i = 0; i < 8; i++)
    {
        k[i] = rand() & 0xffffffff;
    }

    // 计算g = h^((p-1)/q) mod p
    unsigned int p_minus_1[8];
    memcpy(p_minus_1, p, sizeof(p));
    p_minus_1[7] -= 1;
    unsigned int q_minus_1[2];
    memcpy(q_minus_1, q, sizeof(q));
    q_minus_1[1] -= 1;
    unsigned int p_minus_1_div_q[8];
    memcpy(p_minus_1_div_q, p_minus_1, sizeof(p_minus_1));
    for (int i = 0; i < 7; i++)
    {
        p_minus_1_div_q[i] /= q[0];
    }
    p_minus_1_div_q[7] = (p_minus_1_div_q[7] / q[0]) + ((p_minus_1_div_q[7] % q[0]) << 32);
    unsigned int g_temp[8];
    memcpy(g_temp, h, sizeof(h));
    for (int i = 0; i < 8; i++)
    {
        g[i] = 0;
    }
    g[7] = 1;
    for (int i = 0; i < 8 * 32; i++)
    {
        if (((p_minus_1_div_q[i / 32] >> (i % 32)) & 1) != 0)
        {
            unsigned int g_temp2[8];
            memcpy(g_temp2, g_temp, sizeof(g_temp));
            sha1((unsigned char*)g_temp2, sizeof(g_temp2), (unsigned char*)g_temp2);
            for (int j = 0; j < 8; j++)
            {
                g[j] = mul(g[j], g_temp2[j], p[j]);
            }
            unsigned int g_temp2[8];
            memcpy(g_temp2, g_temp, sizeof(g_temp));
            sha1((unsigned char*)g_temp2, sizeof(g_temp2), (unsigned char*)g_temp2);
            for (int j = 0; j < 8; j++)
            {
                g_temp[j] = mul(g_temp[j], g_temp2[j], p[j]);
            }
        }

        // 生成随机数x
        unsigned int max_x[8];
        memcpy(max_x, p_minus_1, sizeof(p_minus_1));
        max_x[7] -= q[0];
        while (true)
        {
            for (int i = 0; i < 8; i++)
            {
                x[i] = rand() & 0xffffffff;
            }
            if (cmp(x, max_x) < 0)
            {
                break;
            }
        }

        // 计算y = g^x mod p
        memcpy(y, g, sizeof(g));
        for (int i = 1; i < 8 * 32; i++)
        {
            unsigned int y_temp[8];
            memcpy(y_temp, y, sizeof(y));
            sha1((unsigned char*)y_temp, sizeof(y_temp), (unsigned char*)y_temp);
            for (int j = 0; j < 8; j++)
            {
                y[j] = mul(y[j], y_temp[j], p[j]);
            }
            if (((x[i / 32] >> (i % 32)) & 1) != 0)
            {
                unsigned int y_temp2[8];
                memcpy(y_temp2, y, sizeof(y));
                sha1((unsigned char*)y_temp2, sizeof(y_temp2), (unsigned char*)y_temp2);
                for (int j = 0; j < 8; j++)
                {
                    y[j] = mul(y[j], y_temp2[j], p[j]);
                }
            }
        }
    }
}

// 判断一个数是否为素数
bool is_prime(unsigned int n)
{
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    unsigned int i = 5;
    while (i * i <= n)
    {
        if (n % i == 0 || n % (i + 2) == 0) return false;
        i += 6;
    }

    return true;
}

int main()
{
    // 用户输入p、q、h
    unsigned int p[8], q[2], h[8];
    cout << "请输入一个160位的素数q（以16进制格式输入）：" << endl;
    cin >> hex >> q[0] >> q[1];
    if (!is_prime(q[0]) || !is_prime(q[1]))
    {
        cout << "q必须为素数！" << endl;
        return 0;
    }
    if (((q[0] & 0x80000000) != 0) || ((q[1] & 0x80000000) != 0) || ((q[1] & 0x40000000) == 0))
    {
        cout << "q必须满足2^159 < q < 2^160！" << endl;
        return 0;
    }

    cout << "请输入一个512~1024位的素数p，且p-1是q的倍数（以16进制格式输入）：" << endl;
    cin >> hex >> p[0] >> p[1] >> p[2] >> p[3] >> p[4] >> p[5] >> p[6] >> p[7];
    if (!is_prime(p[0]) || ((p[0] - 1) % q[0] != 0) || ((p[0] - 1) % q[1] != 0))
    {
        cout << "p必须是q的倍数且为素数！" << endl;
        return 0;
    }

    cout << "请输入一个160位的h（以16进制格式输入）：" << endl;
    cin >> hex >> h[0] >> h[1] >> h[2] >> h[3] >> h[4] >> h[5] >> h[6] >> h[7];

    // 生成DSA参数
    unsigned int x[8], y[8], g[8];
    generate_dsa_params(p, q, h, x, y, g);

    // 输出DSA参数
    cout << "p = " << hex << p[0] << p[1] << p[2] << p[3] << p[4] << p[5] << p[6] << p[7] << endl;
    cout << "q = " << hex << q[0] << q[1] << endl;
    cout << "h = " << hex << h[0] << h[1] << h[2] << h[3] << h[4] << h[5] << h[6] << h[7] << endl;
    cout << "x = " << hex << x[0] << x[1] << x[2] << x[3] << x[4] << x[5] << x[6] << x[7] << endl;
    cout << "y = " << hex << y[0] << y[1] << y[2] << y[3] << y[4] << y[5] << y[6] << y[7] << endl;
    cout << "g = " << hex << g[0] << g[1] << g[2] << g[3] << g[4] << g[5] << g[6] << g[7] << endl;

    return 0;
}