"""quick_sort.py

A Python port of the quicksort example for our DSA class.
Adapted from the code provided with:
  Java Foundations (2nd & 3rd ed) by Lewis, DePasquale, & Chase
  Algorithms (4th ed) by Sedgewick & Wayne

Run:
  python quick_sort.py
"""

import random


# ---- Helper operations -------------------------------------------------
# These operations occur multiple times in our sorting routines,
#   so we pull them out into small helpers.

def swap(data, ii, jj):
    data[ii], data[jj] = data[jj], data[ii]


def is_sorted(data, lo=0, hi=None):
    if hi is None:
        hi = len(data) - 1
    for ii in range(lo + 1, hi + 1):
        if data[ii] < data[ii - 1]:
            return False
    return True


# ---- Quicksort ---------------------------------------------------------

def partition(data, lo, hi):
    middle = lo + ((hi - lo) // 2)

    # Use the middle data value as the partition element,
    #   then move it out of the way (into the lo slot) for now.
    partition_element = data[middle]
    swap(data, middle, lo)

    left = lo
    right = hi

    while left < right:
        # search for an element that is > the partition element
        while left < right and data[left] <= partition_element:
            left += 1

        # search for an element that is < the partition element
        while data[right] > partition_element:
            right -= 1

        # swap the elements
        if left < right:
            swap(data, left, right)

    # move the partition element into place
    swap(data, lo, right)

    return right


def quick_sort(data, lo=0, hi=None):
    if hi is None:
        hi = len(data) - 1

    if lo < hi:
        # create partitions
        index_of_partition = partition(data, lo, hi)

        # sort the left partition (lower values)
        quick_sort(data, lo, index_of_partition - 1)

        # sort the right partition (higher values)
        quick_sort(data, index_of_partition + 1, hi)


# ---- Test harness ------------------------------------------------------

def print_array(a):
    print(" ".join(str(value) for value in a))


def main():
    failures = 0

    for _ in range(5):
        a = [random.randint(0, 999) for _ in range(100)]

        print("\nUnsorted: ", end="")
        print_array(a)

        quick_sort(a)

        print("  Sorted: ", end="")
        print_array(a)

        if not is_sorted(a):
            print("Fail!")
            failures += 1

    print()
    if failures == 0:
        print(f"Test successful! ({failures} failures)")
    else:
        print(f"Test unsuccessful! ({failures} failures)")


if __name__ == "__main__":
    main()
