#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstring>

using namespace std;

const unsigned int kSHA1HashSize = 20;

class SHA1 {
public:
    SHA1() {
        H[0] = 0x67452301;
        H[1] = 0xEFCDAB89;
        H[2] = 0x98BADCFE;
        H[3] = 0x10325476;
        H[4] = 0xC3D2E1F0;
    }

    void update(const char* data, size_t length) {
        uint32_t* data32 = (uint32_t*)data;
        size_t i = 0;
        while (length >= 64) {
            transform(data32 + i * 16);
            length -= 64;
            i++;
        }
        memcpy(buffer, data32 + i * 16, length);
        buffer_len = length;
    }

    void final(unsigned char hash[kSHA1HashSize]) {
        uint32_t bit_count[2];
        bit_count[0] = total_len * 8;
        bit_count[1] = (total_len >> 29) * 8;
        unsigned char padding[64];
        memset(padding, 0, sizeof(padding));
        padding[0] = 0x80;
        update((const char*)padding, 1 + ((119 - total_len) % 64));
        update((const char*)bit_count, 8);
        for (int i = 0; i < kSHA1HashSize; i += 4) {
            hash[i] = (H[i / 4] >> 24) & 0xff;
            hash[i + 1] = (H[i / 4] >> 16) & 0xff;
            hash[i + 2] = (H[i / 4] >> 8) & 0xff;
            hash[i + 3] = H[i / 4] & 0xff;
        }
    }

private:
    uint32_t H[5];
    size_t total_len = 0;
    unsigned char buffer[64];
    size_t buffer_len = 0;

    void transform(uint32_t* data) {
        uint32_t a = H[0];
        uint32_t b = H[1];
        uint32_t c = H[2];
        uint32_t d = H[3];
        uint32_t e = H[4];
        uint32_t temp;
        for (int i = 0; i < 80; i++) {
            if (i < 16) {
                temp = data[i];
            }
            else {
                temp = data[(i + 13) & 15] ^ data[(i + 8) & 15] ^ data[(i + 2) & 15] ^ data[i & 15];
                temp = (temp << 1) | (temp >> 31);
            }
            if (i < 20) {
                temp += (e + ((b & c) | (~b & d)) + 0x5A827999);
            }
            else if (i < 40) {
                temp += (e + (b ^ c ^ d) + 0x6ED9EBA1);
            }
            else if (i < 60) {
                temp += (e + ((b & c) | (b & d) | (c & d)) + 0x8F1);
            }
            else {
                temp += (e + (b ^ c ^ d) + 0xCA62C1D6);
            }
            e = d;
            d = c;
            c = (b << 30) | (b >> 2);
            b = a;
            a = temp;
        }
        H[0] += a;
        H[1] += b;
        H[2] += c;
        H[3] += d;
        H[4] += e;
    }
};

string sha1(const string& input) {
    SHA1 sha1;
    sha1.update(input.c_str(), input.size());
    unsigned char hash[kSHA1HashSize];
    sha1.final(hash);
    ostringstream oss;
    for (int i = 0; i < kSHA1HashSize; i++) {
        oss << hex << setfill('0') << setw(2) << (int)hash[i];
    }
    return oss.str();
}

int main() {
    string input = "This is a DSA algorithm";
    string hashed = sha1(input);
    cout << "SHA1 hash of " << input << " is " << hashed << endl;
    return 0;
}