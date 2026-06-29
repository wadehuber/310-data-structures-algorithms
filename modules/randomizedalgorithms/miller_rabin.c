/*
 * Miller-Rabin Primality Test  (CSC310 Module 13 - Randomized Algorithms)
 * ======================================================================
 *
 * In C the interesting wrinkle is overflow: (a * b) for 64-bit a, b overflows
 * unsigned long long, so we use __int128 for the modular multiply.  With the
 * fixed base set below the test is deterministic and correct for all 64-bit n.
 *
 * Build:  gcc -O2 miller_rabin.c -o miller_rabin && ./miller_rabin
 */
#include <stdio.h>
#include <stdint.h>

typedef unsigned long long u64;

/* (a * b) mod m without overflow, via 128-bit intermediate. */
static u64 mulmod(u64 a, u64 b, u64 m) {
    return (u64)((__uint128_t)a * b % m);
}

/* (base^exp) mod m by fast exponentiation. */
static u64 powmod(u64 base, u64 exp, u64 m) {
    u64 result = 1 % m;
    base %= m;
    while (exp > 0) {
        if (exp & 1) result = mulmod(result, base, m);
        base = mulmod(base, base, m);
        exp >>= 1;
    }
    return result;
}

static int is_probable_prime(u64 n) {
    if (n < 2) return 0;
    for (u64 p = 2; p <= 3; p++) {
        if (n == p) return 1;
        if (n % p == 0) return 0;
    }
    /* write n - 1 = d * 2^r, d odd */
    u64 d = n - 1;
    int r = 0;
    while ((d & 1) == 0) { d >>= 1; r++; }

    /* deterministic for all n < 3.3e24 */
    u64 bases[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int i = 0; i < 12; i++) {
        u64 a = bases[i];
        if (a >= n) continue;
        u64 x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        int composite = 1;
        for (int j = 0; j < r - 1; j++) {
            x = mulmod(x, x, n);
            if (x == n - 1) { composite = 0; break; }
        }
        if (composite) return 0;   /* a is a witness */
    }
    return 1;
}

int main(void) {
    u64 samples[] = {561ULL, 1105ULL, 1729ULL, 997ULL, 7919ULL, 9973ULL,
                     104729ULL, (1ULL << 61) - 1};
    int n = sizeof(samples) / sizeof(samples[0]);
    printf("%22s  %s\n", "n", "Miller-Rabin");
    printf("--------------------------------------\n");
    for (int i = 0; i < n; i++) {
        printf("%22llu  %s\n", samples[i],
               is_probable_prime(samples[i]) ? "prime" : "composite");
    }
    return 0;
}
