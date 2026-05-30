"""
Heap construction: O(n log n) naive insertion vs O(n) bottom-up heapify.

Two ways to turn an unordered array into a valid (min-)heap:

  1. NAIVE   - start with an empty heap and insert() each element one at a
               time. Every insert may sift the new element UP toward the
               root, costing O(log n), so n inserts cost O(n log n).

  2. HEAPIFY - drop all n elements into the array as-is, then sift_down()
               each internal node, starting from the last one and moving
               toward the root. Surprisingly, this is O(n) -- linear.

The "obvious" intuition says heapify must ALSO be O(n log n): we call
sift_down on ~n/2 nodes, and sift_down is O(log n), so n/2 * log n =
O(n log n). That intuition is WRONG, and this file shows why -- both with a
proof sketch (see explain()) and with an experiment that counts the actual
swaps each method performs (see run_experiment()).
"""

from typing import List


# ---------------------------------------------------------------------------
# A tiny min-heap that COUNTS the swaps it performs, so we can measure work.
# ---------------------------------------------------------------------------
class CountingMinHeap:
    def __init__(self) -> None:
        self.data: List[int] = []
        self.swaps = 0                       # how many element swaps we've done

    def _swap(self, i: int, j: int) -> None:
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.swaps += 1

    def _sift_up(self, i: int) -> None:
        """Move element at index i UP until the heap property holds.
        Cost = distance to the root in the worst case = O(log n)."""
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i: int, size: int) -> None:
        """Move element at index i DOWN until the heap property holds.
        Cost = the node's HEIGHT, not the height of the whole tree."""
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    # --- strategy 1: naive insertion, O(n log n) ---------------------------
    def build_naive(self, items: List[int]) -> None:
        self.data = []
        self.swaps = 0
        for x in items:
            self.data.append(x)                 # put new element at the end...
            self._sift_up(len(self.data) - 1)   # ...then bubble it up.

    # --- strategy 2: bottom-up heapify, O(n) -------------------------------
    def build_heapify(self, items: List[int]) -> None:
        self.data = list(items)                 # all elements in place at once
        self.swaps = 0
        n = len(self.data)

        # In a 0-indexed array heap:
        #   left child  = 2*i + 1
        #   right child = 2*i + 2
        #
        # Any index from n//2 through n-1 is a leaf, because its left child
        # would be outside the array. Leaves are already valid 1-element heaps,
        # so bottom-up heapify starts at the last internal node: n//2 - 1.
        last_internal = n // 2 - 1

        for i in range(last_internal, -1, -1):
            self._sift_down(i, n)

    def is_valid_min_heap(self) -> bool:
        n = len(self.data)
        for i in range(n):
            for child in (2 * i + 1, 2 * i + 2):
                if child < n and self.data[child] < self.data[i]:
                    return False
        return True


# ---------------------------------------------------------------------------
# Experiment: count the real swaps each method does as n grows.
# ---------------------------------------------------------------------------
def run_experiment() -> None:
    print("MEASURED WORK (number of element swaps during construction)")
    print("Input: a strictly DECREASING sequence -- the worst case for naive")
    print("insertion into a min-heap (every new element is the new minimum and")
    print("must bubble from a leaf all the way to the root).\n")

    header = f"{'n':>9} | {'naive swaps':>13} {'/n':>7} | {'heapify swaps':>14} {'/n':>6}"
    print(header)
    print("-" * len(header))

    n = 1000
    while n <= 128_000:
        descending_input = list(range(n, 0, -1))          # n, n-1, ..., 2, 1
        heap = CountingMinHeap()

        heap.build_naive(descending_input)
        naive_swaps = heap.swaps
        assert heap.is_valid_min_heap()

        heap.build_heapify(descending_input)
        heapify_swaps = heap.swaps
        assert heap.is_valid_min_heap()

        print(f"{n:>9} | {naive_swaps:>13,} {naive_swaps / n:>7.2f} | "
              f"{heapify_swaps:>14,} {heapify_swaps / n:>6.2f}")
        n *= 2

    print("\nRead the '/n' columns -- they are swaps PER element:")
    print("  * naive   /n keeps CLIMBING (roughly +1 each time n doubles).")
    print("            That growing-with-log(n) factor is the n log n cost.")
    print("  * heapify /n stays FLAT and below 1. Constant work per element")
    print("            is exactly what O(n) looks like.")

# ---------------------------------------------------------------------------
# Small hand trace: show what heapify does on a tiny input.
# ---------------------------------------------------------------------------
def show_small_example() -> None:
    print("SMALL HEAPIFY EXAMPLE")
    print("=====================")

    items = [7, 6, 5, 4, 3, 2, 1]
    heap = CountingMinHeap()

    print(f"Original array: {items}")

    heap.build_heapify(items)

    print(f"After heapify:  {heap.data}")
    print(f"Valid min-heap? {heap.is_valid_min_heap()}")
    print(
        "\nThis final array does not have to be sorted.\n"
        "It only has to satisfy the min-heap property:\n"
        "every parent is less than or equal to its children.\n"
    )

# ---------------------------------------------------------------------------
# The math: why does the log factor vanish for heapify?
# ---------------------------------------------------------------------------
def explain() -> None:
    print("\nWHY HEAPIFY IS LINEAR")
    print("=====================")
    print(
        "The naive intuition: 'we call sift_down on ~n/2 nodes and each is\n"
        "O(log n), so the total must be O(n log n).' This over-counts, because\n"
        "sift_down's cost is a node's HEIGHT, and almost every node is short.\n"
        "\n"
        "In a heap of n nodes there are about n/2 leaves (height 0, cost 0),\n"
        "n/4 nodes of height 1, n/8 of height 2, ... and only ONE node -- the\n"
        "root -- with the full height log n. Summing (count * height):\n"
        "\n"
        "    total work  <=  sum over h>=0 of  (n / 2^(h+1)) * h\n"
        "                 =  (n / 2) * sum over h>=0 of  h / 2^h\n"
        "                 =  (n / 2) * 2\n"
        "                 =  n                 ->   O(n)\n"
        "\n"
        "The series  sum h/2^h  converges to the constant 2, so the would-be\n"
        "log n factor collapses. The many CHEAP leaves dominate the count; the\n"
        "few EXPENSIVE nodes near the root are too rare to matter.\n"
        "\n"
        "Contrast with naive insertion: there the expensive direction is\n"
        "sift-UP, and the numerous bottom-level elements are exactly the ones\n"
        "that can travel the full height up to the root. The costs line up the\n"
        "wrong way, and you genuinely pay O(n log n).\n"
        "\n"
        "Lesson: 'n operations, each O(log n)' is an UPPER bound, not the\n"
        "answer. When the per-operation cost varies, you must sum the actual\n"
        "costs -- intuition that multiplies worst-case-per-step by step-count\n"
        "can badly mislead you."
    )


if __name__ == "__main__":
    print("Small example:")
    show_small_example()
    print()
    run_experiment()
    explain()
