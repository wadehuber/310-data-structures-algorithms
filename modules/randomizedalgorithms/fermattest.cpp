/*
 * Fermat Primality Test (Randomized Algorithm)
 *
 * A probabilistic primality test based on Fermat's Little Theorem. For a prime n,
 * a^(n-1) ≡ 1 (mod n) for all 1 < a < n. This test checks this property for
 * random values of a. If the test fails for any a, n is definitely composite.
 * If it passes for all trials, n is probably prime.
 *
 * Time Complexity: O(k log^3 n) where k = number of trials
 * Space Complexity: O(1)
 *
 * Based on CLRS Chapter 31 - Number-Theoretic Algorithms
 */

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Fast modular exponentiation: computes (base^exp) % mod
long long modPow(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;

    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }

    return result;
}

// Fermat primality test
bool fermatTest(int n, int trials = 5) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0) return false;

    for (int i = 0; i < trials; i++) {
        int a = 2 + rand() % (n - 3);  // random integer in [2, n-2]
        if (modPow(a, n - 1, n) != 1) {
            return false; // definitely composite
        }
    }

    return true; // probably prime
}

int main() {
    srand(time(0));

    int nums[] = {10, 17, 21, 122, 561, 997};
    for (int n : nums) {
        cout << n << ": ";
        if (fermatTest(n)) {
            cout << "probably prime" << endl;
        } else {
            cout << "composite" << endl;
        }
    }

    return 0;
}