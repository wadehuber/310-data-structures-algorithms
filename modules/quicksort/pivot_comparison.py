"""pivot_comparison.py

How does the *choice of pivot* affect quicksort?

Quicksort's performance lives or dies by how evenly each partition step
splits the data.  A good pivot lands near the median, giving two roughly
equal halves and O(n log n) behavior.  A bad pivot peels off one element at
a time, degrading to O(n^2) -- and, because this implementation recurses,
that also means O(n) recursion depth, which can blow the stack on already
sorted input.

This script implements quicksort once, parameterized by a *pivot strategy*,
counts the number of comparisons each strategy makes, and runs every
strategy against several input shapes (random, already-sorted, reverse
sorted, all-equal).  The comparison count is the interesting number: it is
deterministic for a given input + strategy and is proportional to the real
work quicksort does.

Run:
  python pivot_comparison.py
"""

import random
import sys


# ---- Instrumented quicksort -------------------------------------------
# We pass around a one-element list `counter` so the recursive calls can all
# bump the same comparison tally.  `choose_pivot` is a function that, given
# the slice bounds, returns the index to use as the pivot.

def quick_sort(data, choose_pivot):
    counter = [0]
    _quick_sort(data, 0, len(data) - 1, choose_pivot, counter)
    return counter[0]


def _quick_sort(data, lo, hi, choose_pivot, counter):
    if lo < hi:
        p = _partition(data, lo, hi, choose_pivot, counter)
        _quick_sort(data, lo, p - 1, choose_pivot, counter)
        _quick_sort(data, p + 1, hi, choose_pivot, counter)


def _partition(data, lo, hi, choose_pivot, counter):
    # Ask the strategy which index to use, then swap it to the front so the
    # partition logic below is identical for every strategy.
    pivot_index = choose_pivot(data, lo, hi)
    data[pivot_index], data[lo] = data[lo], data[pivot_index]

    pivot = data[lo]
    left = lo
    right = hi

    while left < right:
        while left < right:
            counter[0] += 1
            if data[left] <= pivot:
                left += 1
            else:
                break
        while right > lo:
            counter[0] += 1
            if data[right] > pivot:
                right -= 1
            else:
                break
        if left < right:
            data[left], data[right] = data[right], data[left]

    data[lo], data[right] = data[right], data[lo]
    return right


# ---- Pivot strategies -------------------------------------------------
# Each strategy receives (data, lo, hi) and returns an index in [lo, hi].

def pivot_first(data, lo, hi):
    return lo


def pivot_last(data, lo, hi):
    return hi


def pivot_middle(data, lo, hi):
    return lo + (hi - lo) // 2


def pivot_random(data, lo, hi):
    return random.randint(lo, hi)


def pivot_median_of_three(data, lo, hi):
    """Look at the first, middle, and last elements and pick the one whose
    value is the median of the three.  Cheap, and a very effective guard
    against the sorted / reverse-sorted worst cases."""
    mid = lo + (hi - lo) // 2
    a, b, c = data[lo], data[mid], data[hi]
    if a <= b <= c or c <= b <= a:
        return mid
    if b <= a <= c or c <= a <= b:
        return lo
    return hi


STRATEGIES = [
    ("first element", pivot_first),
    ("last element", pivot_last),
    ("middle element", pivot_middle),
    ("random element", pivot_random),
    ("median of three", pivot_median_of_three),
]


# ---- Input shapes -----------------------------------------------------

def make_inputs(n):
    return [
        ("random", [random.randint(0, n * 10) for _ in range(n)]),
        ("already sorted", list(range(n))),
        ("reverse sorted", list(range(n, 0, -1))),
        ("all equal", [42] * n),
    ]


# ---- Driver -----------------------------------------------------------

def main():
    n = 500

    # The recursive worst case (sorted input + end-element pivot) needs a
    # recursion depth of ~n, so lift Python's limit for the demo.
    sys.setrecursionlimit(10 * n + 1000)

    inputs = make_inputs(n)

    print(f"Quicksort comparison counts (n = {n})")
    print("Lower is better. ~n*log2(n) ~= "
          f"{int(n * (n.bit_length()))} is roughly the 'good' target;"
          f" n^2/2 = {n * n // 2} is the worst case.\n")

    # Header row.
    name_width = max(len(name) for name, _ in STRATEGIES)
    header = "pivot strategy".ljust(name_width)
    for shape_name, _ in inputs:
        header += "  " + shape_name.rjust(14)
    print(header)
    print("-" * len(header))

    for strat_name, choose_pivot in STRATEGIES:
        row = strat_name.ljust(name_width)
        for _, base in inputs:
            data = list(base)  # fresh, unsorted copy for each run
            try:
                comparisons = quick_sort(data, choose_pivot)
                assert data == sorted(base), "sort produced wrong result!"
                cell = f"{comparisons:,}"
            except RecursionError:
                cell = "STACK OVERFLOW"
            row += "  " + cell.rjust(14)
        print(row)

    print(
        "\nTakeaways:\n"
        "  * 'first' and 'last' explode to the O(n^2) worst case on the\n"
        "    sorted / reverse-sorted inputs they are most likely to meet in\n"
        "    practice -- and the deep recursion can overflow the stack.\n"
        "  * 'middle' dodges those particular adversaries but still has\n"
        "    pathological inputs that can be constructed against it.\n"
        "  * 'random' and 'median of three' stay close to the n*log(n)\n"
        "    target across every input shape, which is why real libraries\n"
        "    use strategies like these (often combined).\n"
        "  * 'all equal' is worst-case for EVERY strategy here: pivot choice\n"
        "    cannot help when all keys are identical.  Beating that case\n"
        "    needs a different idea -- three-way ('Dutch national flag')\n"
        "    partitioning, which groups equal keys in the middle."
    )


if __name__ == "__main__":
    main()
