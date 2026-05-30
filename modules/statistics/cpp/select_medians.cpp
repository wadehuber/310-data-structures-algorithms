// Deterministic Selection (Median of Medians)
// --------------------------------------------
// The SELECT algorithm from the "Medians & Order Statistics" notes -- the
// worst-case O(n) selection algorithm, in contrast to RANDOMIZED-SELECT
// (randselect.cpp), which is only O(n) *expected*.
//
// The trick is choosing a provably good pivot instead of a random one:
//   1. Split the elements into groups of 5.
//   2. Find each group's median (by sorting the tiny group).
//   3. Recursively SELECT the median OF those medians.
//   4. Partition around that "median of medians" -- it is guaranteed to be
//      far enough from the extremes that each recursive call shrinks the
//      problem by a constant fraction, which keeps the worst case linear.
//
// As the notes point out, this guarantee comes with larger constant factors,
// so in practice quickselect is usually preferred -- a classic case of
// theoretical optimality not matching real-world speed.

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

// Return the i-th smallest element of `data` (1-based) in worst-case O(n).
int median_of_medians_select(std::vector<int> data, int i) {
    int n = static_cast<int>(data.size());
    if (n <= 5) {
        std::sort(data.begin(), data.end());
        return data[i - 1];
    }

    // Step 1-2: median of each group of 5.
    std::vector<int> medians;
    for (int start = 0; start < n; start += 5) {
        int end = std::min(start + 5, n);
        std::vector<int> group(data.begin() + start, data.begin() + end);
        std::sort(group.begin(), group.end());
        medians.push_back(group[(group.size() - 1) / 2]);
    }

    // Step 3: median of the medians (recursively).
    int pivot = median_of_medians_select(medians, (static_cast<int>(medians.size()) + 1) / 2);

    // Step 4: partition around the pivot and recurse into one side only.
    std::vector<int> less, equal, greater;
    for (int x : data) {
        if (x < pivot) less.push_back(x);
        else if (x > pivot) greater.push_back(x);
        else equal.push_back(x);
    }

    if (i <= static_cast<int>(less.size())) {
        return median_of_medians_select(less, i);
    } else if (i <= static_cast<int>(less.size() + equal.size())) {
        return pivot;                                   // pivot is the answer
    } else {
        int new_i = i - static_cast<int>(less.size() + equal.size());
        return median_of_medians_select(greater, new_i);
    }
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
    std::vector<int> A = {25, 3, 41, 17, 9, 38, 2, 14, 30, 7,
                          22, 11, 36, 5, 19, 28, 1, 33, 16};
    std::cout << "Array: ";
    print_vector(A);
    std::cout << "\n\n";

    std::vector<int> ordered = A;
    std::sort(ordered.begin(), ordered.end());

    int n = static_cast<int>(A.size());
    int ranks[] = {1, n / 2 + 1, n};
    for (int i : ranks) {
        int got = median_of_medians_select(A, i);
        const char* label = (i == n / 2 + 1) ? "median" : (i == 1 ? "min" : "max");
        std::printf("%2dth smallest (%6s): %d   (sorted check: %d)\n",
                    i, label, got, ordered[i - 1]);
    }

    std::cout << "\n";
    // Confirm it agrees with a full sort for all ranks.
    bool all_match = true;
    for (int i = 1; i <= n; i++) {
        if (median_of_medians_select(A, i) != ordered[i - 1]) {
            all_match = false;
            break;
        }
    }
    std::cout << "Matches sorted order for every rank: "
              << (all_match ? "true" : "false") << "\n";

    return 0;
}
