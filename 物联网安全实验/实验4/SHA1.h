#pragma once
#include <iostream>
#include <cstring>

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