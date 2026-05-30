"""
Counting Sort
-------------
A demonstration of the stable counting sort described in the
"Sorting in Linear Time" notes.

Counting sort works when the input is integers in a small, known range
{0, 1, ..., k}.  It runs in Theta(n + k) time, which is linear when k = O(n).

This example sorts a list of small integer "class labels" -- the kind of
bounded-range data the notes mention (one-hot category indices, histogram
bins, discretized features) -- so you can watch the three passes in action.
"""


def counting_sort(A, k):
    """
    Return a sorted copy of A, where every element is an integer in 0..k.

    Mirrors the stable pseudocode from the notes:
      1. Count occurrences of each value.
      2. Turn counts into cumulative end-positions.
      3. Place elements right-to-left to keep equal keys stable.
    """
    n = len(A)
    C = [0] * (k + 1)          # C[v] will count how many times v appears
    B = [0] * n                # output array

    # Pass 1: tally each value.
    for value in A:
        C[value] += 1

    # Pass 2: cumulative sums -> C[v] is the ending position of value v.
    for v in range(1, k + 1):
        C[v] += C[v - 1]

    # Pass 3: walk right-to-left so equal keys keep their original order.
    for j in range(n - 1, -1, -1):
        value = A[j]
        C[value] -= 1
        B[C[value]] = value

    return B


def counting_sort_pairs(pairs, k):
    """
    Stable counting sort on (key, tag) pairs, keyed by the integer `key`.

    The `tag` carries along unchanged so you can SEE stability: items with
    the same key come out in the same order they went in.  This stability is
    exactly the property radix sort relies on.
    """
    n = len(pairs)
    C = [0] * (k + 1)
    B = [None] * n

    for key, _tag in pairs:
        C[key] += 1
    for v in range(1, k + 1):
        C[v] += C[v - 1]
    for j in range(n - 1, -1, -1):
        key = pairs[j][0]
        C[key] -= 1
        B[C[key]] = pairs[j]

    return B


def main():
    # Bounded-range integer labels (values 0..5).
    labels = [3, 0, 5, 2, 3, 1, 0, 4, 2, 3, 5, 1, 0]
    k = 5

    print("Input labels:", labels)
    print("Counting sorted:", counting_sort(labels, k))
    print("Python sorted():", sorted(labels))
    print()

    # Show stability: each pair is (key, arrival_order).
    # After sorting by key, equal keys must stay in arrival order.
    pairs = [(2, "a"), (1, "b"), (2, "c"), (0, "d"), (1, "e"), (2, "f")]
    print("Input pairs:  ", pairs)
    print("Stable sorted:", counting_sort_pairs(pairs, k=2))
    print("Notice the (2, ...) items stay in a, c, f order -> stable.")


if __name__ == "__main__":
    main()
