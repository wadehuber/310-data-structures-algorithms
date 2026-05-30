// Mean vs. Median: A Robustness Illustration
// -------------------------------------------
// A demonstration of the "Robust Statistics" idea from the "Medians & Order
// Statistics" notes:
//
//     Mean is sensitive to values.  Median is sensitive only to order.
//
// This program computes both, then injects a single extreme value and
// recomputes, so you can see the mean lurch toward the outlier while the
// median barely moves.  That is the whole point of calling the median
// *robust*: a small fraction of extreme values cannot significantly change it.
//
// (Computing the median here uses a sort for clarity.  As the notes explain --
// and as select_medians.cpp / randselect.cpp show -- the median can actually
// be found in Theta(n) time without fully sorting.)

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

// Arithmetic mean: sum of values divided by count. Uses every value.
double mean(const std::vector<double>& data) {
    double sum = 0.0;
    for (double x : data) sum += x;
    return sum / data.size();
}

// Middle value after ordering.  Depends only on relative order, not on how
// large the extreme values are.
double median(std::vector<double> data) {
    std::sort(data.begin(), data.end());
    size_t n = data.size();
    size_t mid = n / 2;
    if (n % 2 == 1) {
        return data[mid];
    }
    return (data[mid - 1] + data[mid]) / 2.0;
}

void print_vector(const std::vector<double>& v) {
    std::cout << "[";
    for (size_t i = 0; i < v.size(); i++) {
        std::printf("%g", v[i]);
        if (i + 1 < v.size()) std::cout << ", ";
    }
    std::cout << "]";
}

void report(const char* label, const std::vector<double>& data) {
    std::cout << label << "\n";
    std::cout << "  data:   ";
    print_vector(data);
    std::printf("\n  mean:   %.2f\n", mean(data));
    std::printf("  median: %.2f\n\n", median(data));
}

int main() {
    // Server response times in milliseconds: tightly clustered, no outlier.
    std::vector<double> clean = {102, 98, 105, 99, 101, 103, 100, 97, 104};
    report("Clean readings:", clean);

    // One request hit a stall (a 4000 ms spike). Same data plus one outlier.
    std::vector<double> with_outlier = clean;
    with_outlier.push_back(4000);
    report("With one extreme outlier added:", with_outlier);

    double base_mean = mean(clean), base_median = median(clean);
    double out_mean = mean(with_outlier), out_median = median(with_outlier);
    std::cout << "Effect of the single outlier:\n";
    std::printf("  mean   moved by %8.2f ms  (chases the outlier)\n",
                out_mean - base_mean);
    std::printf("  median moved by %8.2f ms  (stays put -> robust)\n",
                out_median - base_median);

    return 0;
}
