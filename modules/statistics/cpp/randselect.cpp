// Randomized Selection (Quickselect)
// ----------------------------------
// RANDOMIZED-SELECT from the "Medians & Order Statistics" notes: find the
// i-th smallest element (1-based) of an array in Theta(n) expected time.
//
// It reuses quicksort's partition, but recurses into only the one side that
// must contain the answer -- so on average it does linear work instead of
// the n log n a full sort would cost.

#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

static std::mt19937 rng(std::random_device{}());

// Standard Lomuto partition scheme.
int partition(std::vector<int>& A, int p, int r) {
    int pivot = A[r];
    int i = p - 1;

    for (int j = p; j < r; j++) {
        if (A[j] <= pivot) {
            i += 1;
            std::swap(A[i], A[j]);
        }
    }

    std::swap(A[i + 1], A[r]);
    return i + 1;
}

// Chooses a random pivot, swaps it with A[r], then partitions the array
// around the pivot.  Returns the final pivot index.
int randomized_partition(std::vector<int>& A, int p, int r) {
    std::uniform_int_distribution<int> dist(p, r);
    int pivot_index = dist(rng);
    std::swap(A[pivot_index], A[r]);
    return partition(A, p, r);
}

// Returns the i-th smallest element of A[p..r] (i is 1-based).
int randomized_select_range(std::vector<int>& A, int p, int r, int i) {
    if (p == r) {
        return A[p];
    }

    int q = randomized_partition(A, p, r);
    int k = q - p + 1;          // rank of pivot within subarray

    if (i == k) {
        return A[q];
    } else if (i < k) {
        return randomized_select_range(A, p, q - 1, i);
    } else {
        return randomized_select_range(A, q + 1, r, i - k);
    }
}

// Returns the i-th smallest element of A (i is 1-based).
int randomized_select(std::vector<int> A, int i) {   // by value: we rearrange it
    return randomized_select_range(A, 0, static_cast<int>(A.size()) - 1, i);
}

void print_vector(const std::vector<int>& v) {
    std::cout << "[";
    for (size_t idx = 0; idx < v.size(); idx++) {
        std::cout << v[idx];
        if (idx + 1 < v.size()) std::cout << ", ";
    }
    std::cout << "]";
}

int main() {
    std::vector<int> A = {13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11};
    int i = 5;  // Find the 5th smallest element

    std::cout << "Original array: ";
    print_vector(A);
    std::cout << "\n";

    int result = randomized_select(A, i);   // passed by value, original untouched
    std::cout << i << "th smallest element: " << result << "\n";

    // Verification.
    std::vector<int> sorted_A = A;
    std::sort(sorted_A.begin(), sorted_A.end());
    std::cout << "Sorted array: ";
    print_vector(sorted_A);
    std::cout << "\nCheck: " << sorted_A[i - 1] << "\n";

    return 0;
}
