// Bucket Sort
// -----------
// A demonstration of bucket sort from the "Sorting in Linear Time" notes.
//
// Bucket sort assumes the input is real numbers uniformly distributed over
// [0, 1).  It divides that range into n equal buckets, drops each element
// into the bucket for its range, sorts each bucket with a simple method
// (insertion sort works well because buckets stay small), and concatenates.
//
// Under the uniform assumption each bucket holds roughly a constant number of
// elements, giving O(n) expected time.
//
// This example sorts uniform [0, 1) scores -- the kind of normalized
// confidence values the notes mention -- and prints the bucket contents so
// you can see the distribute-then-concatenate structure.

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

// Plain insertion sort; fast on the short lists inside each bucket.
void insertion_sort(std::vector<double>& values) {
    for (size_t i = 1; i < values.size(); i++) {
        double key = values[i];
        int j = static_cast<int>(i) - 1;
        while (j >= 0 && values[j] > key) {
            values[j + 1] = values[j];
            j -= 1;
        }
        values[j + 1] = key;
    }
}

void print_vector(const std::vector<double>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        std::printf("%g", v[i]);
        if (i + 1 < v.size()) std::cout << ", ";
    }
    std::cout << "]";
}

// Return a sorted copy of A, where every element is in [0, 1).
// Uses n buckets so that element x lands in bucket floor(n * x).
std::vector<double> bucket_sort(const std::vector<double>& A, bool show_buckets) {
    int n = static_cast<int>(A.size());
    if (n == 0) {
        return {};
    }

    std::vector<std::vector<double>> buckets(n);

    // Distribute: bucket index scales with the value (input is in [0, 1)).
    for (double x : A) {
        int index = static_cast<int>(n * x);
        if (index == n) {   // guard the x == 1.0 edge if it ever appears
            index = n - 1;
        }
        buckets[index].push_back(x);
    }

    // Sort each bucket, then concatenate in order.
    std::vector<double> result;
    result.reserve(n);
    for (int i = 0; i < n; i++) {
        insertion_sort(buckets[i]);
        if (show_buckets) {
            std::printf("  bucket %d [%.2f, %.2f): ", i,
                        static_cast<double>(i) / n,
                        static_cast<double>(i + 1) / n);
            print_vector(buckets[i]);
            std::cout << "\n";
        }
        for (double x : buckets[i]) {
            result.push_back(x);
        }
    }

    return result;
}

int main() {
    std::vector<double> scores = {0.78, 0.17, 0.39, 0.26, 0.72,
                                  0.94, 0.21, 0.12, 0.23, 0.68};

    std::cout << "Input scores: ";
    print_vector(scores);
    std::cout << "\nBuckets:\n";
    std::vector<double> result = bucket_sort(scores, true);
    std::cout << "Bucket sorted:  ";
    print_vector(result);

    std::vector<double> sorted_scores = scores;
    std::sort(sorted_scores.begin(), sorted_scores.end());
    std::cout << "\nLibrary sorted: ";
    print_vector(sorted_scores);
    std::cout << "\n";

    return 0;
}
