// Hash Function Quality Comparison  (CSC310 Module 4B - Hashing)
// =============================================================
//
// Measures (1) distribution: collisions/empty/longest bucket when keys are
// hashed into a prime-sized table, and (2) avalanche: when one input bit flips,
// a good hash flips about half the output bits.
//
// Build:  g++ -std=c++17 -O2 hash_function_comparison.cpp -o hash_function_comparison && ./hash_function_comparison
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>

using std::string;
using std::vector;

const double A = 0.6180339887; // (sqrt(5)-1)/2

int hDivision(long k, int m)       { return (int)(k % m); }
int hMultiplication(long k, int m) { double f = (k * A); f -= (long)f; return (int)(m * f); }
int hShiftFold(long k, int m) {
    string s = std::to_string(k);
    long total = 0;
    for (size_t i = 0; i < s.size(); i += 2) total += std::stol(s.substr(i, 2));
    return (int)(total % m);
}
int hMidSquare(long k, int m) {
    string s = std::to_string((long long)k * k);
    size_t mid = s.size() / 2;
    string chunk = s.substr(mid > 0 ? mid - 1 : 0, 3);
    return (int)(std::stol(chunk) % m);
}
int hFirstDigit(long k, int m) { return (std::to_string(k)[0] - '0') % m; }

// ---- 32-bit hashes for the avalanche test ----
uint32_t mix32(uint32_t k) {       // good
    k *= 2654435761u; k ^= k >> 16;
    k *= 2246822519u; k ^= k >> 13;
    return k;
}
uint32_t weak32(uint32_t k) { return k * 3u; }  // poor: low bits only

double avalanche(uint32_t (*h)(uint32_t), int trials = 4000) {
    std::mt19937 rng(0);
    long flips = 0;
    for (int t = 0; t < trials; ++t) {
        uint32_t k = rng(), base = h(k);
        int bit = rng() % 32;
        uint32_t diff = base ^ h(k ^ (1u << bit));
        flips += __builtin_popcount(diff);
    }
    return (double)flips / trials / 32.0;
}

int main() {
    std::mt19937 rng(7);
    std::uniform_int_distribution<long> keygen(100000, 999999);
    vector<long> keys;
    for (int i = 0; i < 80; ++i) keys.push_back(keygen(rng));
    int m = 97, n = (int)keys.size();
    double expected = n - m * (1 - std::pow((m - 1.0) / m, n));

    struct S { const char* name; int (*h)(long, int); } strat[] = {
        {"division", hDivision}, {"multiplication", hMultiplication},
        {"shift folding", hShiftFold}, {"mid-square", hMidSquare},
        {"first digit (poor)", hFirstDigit},
    };

    std::cout << "Distribution of " << n << " keys into a table of size " << m
              << " (ideal uniform hash collides ~" << (int)std::lround(expected) << " times):\n";
    std::cout << "  " << std::left << std::setw(20) << "strategy" << std::right
              << std::setw(6) << "used" << std::setw(7) << "empty"
              << std::setw(10) << "max load" << std::setw(12) << "collisions" << "\n";
    std::cout << "  " << string(55, '-') << "\n";
    for (auto& s : strat) {
        vector<int> b(m, 0);
        for (long k : keys) b[s.h(k, m)]++;
        int used = 0, mx = 0;
        for (int x : b) { if (x) used++; mx = std::max(mx, x); }
        std::cout << "  " << std::left << std::setw(20) << s.name << std::right
                  << std::setw(6) << used << std::setw(7) << (m - used)
                  << std::setw(10) << mx << std::setw(12) << (n - used) << "\n";
    }
    std::cout << "\nAvalanche (fraction of 32 output bits that flip per input-bit flip;"
                 "\na good hash is near 0.50):\n";
    std::cout << "  mix32 (good multiply + xorshift): " << std::fixed
              << std::setprecision(3) << avalanche(mix32) << "\n";
    std::cout << "  weak32 (low bits only)          : " << avalanche(weak32) << "\n";
    return 0;
}
