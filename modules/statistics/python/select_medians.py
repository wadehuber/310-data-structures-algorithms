"""
Deterministic Selection (Median of Medians)
--------------------------------------------
A demonstration of the SELECT algorithm from the "Medians & Order
Statistics" notes -- the worst-case O(n) selection algorithm, in contrast
to RANDOMIZED-SELECT (quickselect) in randselect.py, which is only O(n)
*expected*.

The trick is choosing a provably good pivot instead of a random one:
  1. Split the elements into groups of 5.
  2. Find each group's median (by sorting the tiny group).
  3. Recursively SELECT the median OF those medians.
  4. Partition around that "median of medians" -- it is guaranteed to be
     far enough from the extremes that each recursive call shrinks the
     problem by a constant fraction, which keeps the worst case linear.

As the notes point out, this guarantee comes with larger constant factors,
so in practice quickselect is usually preferred -- a classic case of
theoretical optimality not matching real-world speed.
"""


def partition_around_value(A, pivot):
    """
    Split A into (less-than, equal-to, greater-than) the given pivot value.
    Returning three lists keeps this example readable; a production version
    would partition in place.
    """
    less, equal, greater = [], [], []
    for x in A:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            greater.append(x)
        else:
            equal.append(x)
    return less, equal, greater


def median_of_medians_select(A, i):
    """
    Return the i-th smallest element of A (1-based) in worst-case O(n).
    """
    n = len(A)
    if n <= 5:
        return sorted(A)[i - 1]

    # Step 1-2: median of each group of 5.
    medians = []
    for start in range(0, n, 5):
        group = A[start:start + 5]
        medians.append(sorted(group)[(len(group) - 1) // 2])

    # Step 3: median of the medians (recursively).
    pivot = median_of_medians_select(medians, (len(medians) + 1) // 2)

    # Step 4: partition around that pivot and recurse into one side only.
    less, equal, greater = partition_around_value(A, pivot)

    if i <= len(less):
        return median_of_medians_select(less, i)
    elif i <= len(less) + len(equal):
        return pivot                                  # pivot is the answer
    else:
        new_i = i - len(less) - len(equal)
        return median_of_medians_select(greater, new_i)


def main():
    A = [25, 3, 41, 17, 9, 38, 2, 14, 30, 7, 22, 11, 36, 5, 19, 28, 1, 33, 16]
    print("Array:", A)
    print()

    # Show selection works for every rank, and matches the sorted order.
    ordered = sorted(A)
    for i in (1, len(A) // 2 + 1, len(A)):
        got = median_of_medians_select(list(A), i)
        label = "median" if i == len(A) // 2 + 1 else ("min" if i == 1 else "max")
        print(f"{i:>2}th smallest ({label:>6}): {got}   (sorted check: {ordered[i - 1]})")

    print()
    # Confirm it agrees with a full sort for all ranks.
    all_match = all(
        median_of_medians_select(list(A), i) == ordered[i - 1]
        for i in range(1, len(A) + 1)
    )
    print("Matches sorted order for every rank:", all_match)


if __name__ == "__main__":
    main()
