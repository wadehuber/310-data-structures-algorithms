// Radix Sort (LSD)
// ----------------
// A demonstration of least-significant-digit radix sort from the
// "Sorting in Linear Time" notes.
//
// Radix sort extends counting sort to multi-digit numbers by sorting one
// digit at a time, from least significant to most significant.  Each pass
// uses a *stable* counting sort as its subroutine, so the ordering achieved
// by earlier (lower) digits survives later passes.
//
// For d-digit numbers in base r it runs in Theta(d * (n + r)) time -- linear
// in the input when the number of digits d is small or constant.
//
// This example sorts fixed-width integer keys (think hashed feature ids or
// quantized values) in base 10 so you can print the array after each digit
// pass and watch it converge.

#include <algorithm>
#include <iostream>
#include <vector>

// Stable counting sort of A using the digit selected by exp.
//
// exp is a power of base: exp=1 sorts by the ones digit, exp=10 by the tens
// digit, and so on.  Stability here is what makes the multi-pass radix sort
// correct.
std::vector<int> counting_sort_by_digit(const std::vector<int>& A, int exp, int base) {
    int n = static_cast<int>(A.size());
    std::vector<int> C(base, 0);
    std::vector<int> B(n, 0);

    // Count occurrences of each digit value (0..base-1).
    for (int value : A) {
        int digit = (value / exp) % base;
        C[digit] += 1;
    }

    // Cumulative sums -> ending positions.
    for (int d = 1; d < base; d++) {
        C[d] += C[d - 1];
    }

    // Place right-to-left to preserve stability.
    for (int j = n - 1; j >= 0; j--) {
        int digit = (A[j] / exp) % base;
        C[digit] -= 1;
        B[C[digit]] = A[j];
    }

    return B;
}

template <typename T>
void print_vector(const std::vector<T>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << v[i];
        if (i + 1 < v.size()) std::cout << ", ";
    }
    std::cout << "]";
}

// Return a sorted copy of A (non-negative integers), one digit pass at a time.
// Set trace=true to print the array after each pass.
std::vector<int> radix_sort(const std::vector<int>& A, int base, bool trace) {
    if (A.empty()) {
        return {};
    }

    std::vector<int> result = A;
    int max_value = *std::max_element(result.begin(), result.end());

    int exp = 1;
    while (max_value / exp > 0) {
        result = counting_sort_by_digit(result, exp, base);
        if (trace) {
            std::cout << "  after ";
            if (exp == 1) {
                std::cout << "  ones digit: ";
            } else {
                std::cout << exp << "s digit: ";
            }
            print_vector(result);
            std::cout << "\n";
        }
        exp *= base;
    }

    return result;
}

int main() {
    std::vector<int> keys = {329, 457, 657, 839, 436, 720, 355, 8, 90, 3};

    std::cout << "Input keys: ";
    print_vector(keys);
    std::cout << "\nRadix sort passes (LSD -> MSD):\n";
    std::vector<int> result = radix_sort(keys, 10, true);
    std::cout << "Radix sorted:   ";
    print_vector(result);

    std::vector<int> sorted_keys = keys;
    std::sort(sorted_keys.begin(), sorted_keys.end());
    std::cout << "\nLibrary sorted: ";
    print_vector(sorted_keys);
    std::cout << "\n";

    return 0;
}
