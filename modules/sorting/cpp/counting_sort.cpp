// Counting Sort
// -------------
// A demonstration of the stable counting sort described in the
// "Sorting in Linear Time" notes.
//
// Counting sort works when the input is integers in a small, known range
// {0, 1, ..., k}.  It runs in Theta(n + k) time, which is linear when k = O(n).
//
// This example sorts a list of small integer "class labels" -- the kind of
// bounded-range data the notes mention (one-hot category indices, histogram
// bins, discretized features) -- so you can watch the three passes in action.

#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

// Return a sorted copy of A, where every element is an integer in 0..k.
//
// Mirrors the stable pseudocode from the notes:
//   1. Count occurrences of each value.
//   2. Turn counts into cumulative end-positions.
//   3. Place elements right-to-left to keep equal keys stable.
std::vector<int> counting_sort(const std::vector<int>& A, int k) {
    int n = static_cast<int>(A.size());
    std::vector<int> C(k + 1, 0);   // C[v] will count how many times v appears
    std::vector<int> B(n, 0);       // output array

    // Pass 1: tally each value.
    for (int value : A) {
        C[value] += 1;
    }

    // Pass 2: cumulative sums -> C[v] is the ending position of value v.
    for (int v = 1; v <= k; v++) {
        C[v] += C[v - 1];
    }

    // Pass 3: walk right-to-left so equal keys keep their original order.
    for (int j = n - 1; j >= 0; j--) {
        int value = A[j];
        C[value] -= 1;
        B[C[value]] = value;
    }

    return B;
}

// Stable counting sort on (key, tag) pairs, keyed by the integer key.
//
// The tag carries along unchanged so you can SEE stability: items with the
// same key come out in the same order they went in.  This stability is
// exactly the property radix sort relies on.
std::vector<std::pair<int, std::string>>
counting_sort_pairs(const std::vector<std::pair<int, std::string>>& pairs, int k) {
    int n = static_cast<int>(pairs.size());
    std::vector<int> C(k + 1, 0);
    std::vector<std::pair<int, std::string>> B(n);

    for (const auto& p : pairs) {
        C[p.first] += 1;
    }
    for (int v = 1; v <= k; v++) {
        C[v] += C[v - 1];
    }
    for (int j = n - 1; j >= 0; j--) {
        int key = pairs[j].first;
        C[key] -= 1;
        B[C[key]] = pairs[j];
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

void print_pairs(const std::vector<std::pair<int, std::string>>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        std::cout << "(" << v[i].first << ", " << v[i].second << ")";
        if (i + 1 < v.size()) std::cout << ", ";
    }
    std::cout << "]";
}

int main() {
    // Bounded-range integer labels (values 0..5).
    std::vector<int> labels = {3, 0, 5, 2, 3, 1, 0, 4, 2, 3, 5, 1, 0};
    int k = 5;

    std::cout << "Input labels: ";
    print_vector(labels);
    std::cout << "\nCounting sorted: ";
    print_vector(counting_sort(labels, k));

    std::vector<int> sorted_labels = labels;
    std::sort(sorted_labels.begin(), sorted_labels.end());
    std::cout << "\nLibrary sorted:  ";
    print_vector(sorted_labels);
    std::cout << "\n\n";

    // Show stability: each pair is (key, arrival_order).
    // After sorting by key, equal keys must stay in arrival order.
    std::vector<std::pair<int, std::string>> pairs = {
        {2, "a"}, {1, "b"}, {2, "c"}, {0, "d"}, {1, "e"}, {2, "f"}};
    std::cout << "Stable sorted: ";
    print_pairs(counting_sort_pairs(pairs, 2));
    std::cout << "\nNotice the (2, ...) items stay in a, c, f order -> stable.\n";

    return 0;
}
