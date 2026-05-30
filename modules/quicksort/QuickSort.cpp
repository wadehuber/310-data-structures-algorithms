// QuickSort.cpp
// A C++ port of the quicksort example for our DSA class.
// Adapted from the code provided with:
//   Java Foundations (2nd & 3rd ed) by Lewis, DePasquale, & Chase
//   Algorithms (4th ed) by Sedgewick & Wayne
//
// Build & run:
//   g++ -std=c++17 -O2 -o QuickSort QuickSort.cpp
//   ./QuickSort

#include <iostream>
#include <vector>
#include <random>

// ---- Helper operations -------------------------------------------------
// These operations occur multiple times in our sorting methods,
//   so we pull them out into small helpers.

template <typename T>
void swap_elements(std::vector<T>& a, int ii, int jj) {
    T tmp = a[ii];
    a[ii] = a[jj];
    a[jj] = tmp;
}

template <typename T>
bool isSorted(const std::vector<T>& data, int min, int max) {
    for (int ii = min + 1; ii <= max; ii++) {
        if (data[ii] < data[ii - 1])
            return false;
    }
    return true;
}

template <typename T>
bool isSorted(const std::vector<T>& data) {
    return isSorted(data, 0, static_cast<int>(data.size()) - 1);
}

// ---- Quicksort ---------------------------------------------------------

template <typename T>
int partition(std::vector<T>& data, int min, int max) {
    int middle = min + ((max - min) / 2);

    // Use the middle data value as the partition element,
    //   then move it out of the way (into the min slot) for now.
    T partitionelement = data[middle];
    swap_elements(data, middle, min);

    int left = min;
    int right = max;

    while (left < right) {
        // search for an element that is > the partition element
        while (left < right && data[left] <= partitionelement)
            left++;

        // search for an element that is < the partition element
        while (data[right] > partitionelement)
            right--;

        // swap the elements
        if (left < right)
            swap_elements(data, left, right);
    }

    // move the partition element into place
    swap_elements(data, min, right);

    return right;
}

template <typename T>
void quickSort(std::vector<T>& data, int min, int max) {
    if (min < max) {
        // create partitions
        int indexofpartition = partition(data, min, max);

        // sort the left partition (lower values)
        quickSort(data, min, indexofpartition - 1);

        // sort the right partition (higher values)
        quickSort(data, indexofpartition + 1, max);
    }
}

template <typename T>
void quickSort(std::vector<T>& data) {
    quickSort(data, 0, static_cast<int>(data.size()) - 1);
}

// ---- Test harness ------------------------------------------------------

template <typename T>
void printArray(const std::vector<T>& a) {
    for (const auto& value : a)
        std::cout << value << " ";
    std::cout << "\n";
}

int main() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(0, 999);

    int failures = 0;

    for (int kk = 0; kk < 5; kk++) {
        std::vector<int> a(100);
        for (auto& value : a)
            value = dist(gen);

        std::cout << "\nUnsorted: ";
        printArray(a);

        quickSort(a);

        std::cout << "  Sorted: ";
        printArray(a);

        if (!isSorted(a)) {
            std::cout << "Fail!\n";
            failures++;
        }
    }

    std::cout << "\n";
    if (failures == 0)
        std::cout << "Test successful! (" << failures << " failures)\n";
    else
        std::cout << "Test unsuccessful! (" << failures << " failures)\n";

    return 0;
}
