"""
CSC310 — Module 01: Algorithm Analysis
Sample implementations in Python.

Covers every algorithm referenced in the module notes:
    - Linear Search                       O(n)        worst case
    - Binary Search (iterative+recursive) O(log n)    worst case
    - Insertion Sort                      O(n^2)      worst case, O(n) best
    - Merge Sort                          Θ(n log n)  all cases
    - Towers of Hanoi                     Θ(2^n)
    - Recursive vs iterative factorial    illustrates stack-space difference
    - Empirical timing demo               connects asymptotic to wall-clock
    - Race-condition demonstration        ties Module 01 to real-world threads

Each function counts its key processing steps (the "basic operation" from
the RAM model in the notes) so we can observe the growth function in action.

Note on indexing: CLRS pseudocode is 1-indexed; Python is 0-indexed.
The algorithms are translated to 0-based indexing here.
"""

from __future__ import annotations
import math
import random
import threading
import time
from typing import Callable


# ---------------------------------------------------------------------------
# 1. LINEAR SEARCH
# ---------------------------------------------------------------------------
# Best:    Θ(1)   — target at index 0
# Average: Θ(n)   — target equally likely anywhere
# Worst:   Θ(n)   — target absent or at last index
# Space:   Θ(1)   — only a loop variable
def linear_search(arr: list, target) -> tuple[int, int]:
    """Return (index_or_-1, comparisons_performed)."""
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons += 1                     # the key processing step
        if value == target:
            return i, comparisons
    return -1, comparisons


# ---------------------------------------------------------------------------
# 2. BINARY SEARCH (requires sorted input — an assumption that must hold!)
# ---------------------------------------------------------------------------
# Best:  Θ(1)      — target is the first midpoint
# Worst: Θ(log n)  — search space halved each iteration
# Space: Θ(1) iterative / Θ(log n) recursive (stack frames)
def binary_search_iterative(arr: list, target) -> tuple[int, int]:
    comparisons = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


def binary_search_recursive(arr: list, target, low: int = 0,
                            high: int | None = None,
                            comparisons: int = 0) -> tuple[int, int]:
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1, comparisons
    mid = (low + high) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    return binary_search_recursive(arr, target, low, mid - 1, comparisons)


# ---------------------------------------------------------------------------
# 3. INSERTION SORT  (CLRS Figure 2.1)
# ---------------------------------------------------------------------------
# Best:  Θ(n)   — already sorted; inner while runs 0 times
# Worst: Θ(n^2) — reverse sorted; inner while runs j-1 times
# Space: Θ(1)  — sorts in-place
def insertion_sort(arr: list) -> int:
    """Sort in-place. Return number of comparisons."""
    comparisons = 0
    # CLRS uses j = 2..length (1-based); Python equivalent is j = 1..len(arr)-1
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0:
            comparisons += 1
            if arr[i] <= key:
                break
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return comparisons


# ---------------------------------------------------------------------------
# 4. MERGE SORT  (divide-and-conquer; CLRS §2.3)
# ---------------------------------------------------------------------------
# Time:  Θ(n log n) in all cases — recurrence T(n) = 2T(n/2) + Θ(n)
# Space: Θ(n)      — temporary arrays for merging (auxiliary space)
def merge_sort(arr: list) -> tuple[list, int]:
    """Return (sorted_copy, comparisons)."""
    comparisons = [0]

    def _merge(left: list, right: list) -> list:
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def _sort(a: list) -> list:
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        return _merge(_sort(a[:mid]), _sort(a[mid:]))

    return _sort(arr), comparisons[0]


# ---------------------------------------------------------------------------
# 5. TOWERS OF HANOI
# ---------------------------------------------------------------------------
# Recurrence: T(n) = 2 T(n - 1) + 1  with T(1) = 1   →   T(n) = 2^n - 1
# Time:  Θ(2^n)      — exponential blowup illustrates why doubling CPU speed
#                      lets us solve only one more disk
# Space: Θ(n) stack — call stack depth equals the number of disks
def towers_of_hanoi(n: int, source: str = "A", target: str = "C",
                    auxiliary: str = "B",
                    moves: list | None = None) -> list:
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
        return moves
    towers_of_hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    towers_of_hanoi(n - 1, auxiliary, target, source, moves)
    return moves


# ---------------------------------------------------------------------------
# 6. RECURSIVE vs ITERATIVE — illustrates Θ(n) stack vs Θ(1) stack
# ---------------------------------------------------------------------------
def factorial_recursive(n: int) -> int:
    """Θ(n) time, Θ(n) stack space. Risk of RecursionError for large n."""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Θ(n) time, Θ(1) extra space."""
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


# ---------------------------------------------------------------------------
# 7. EMPIRICAL TIMING DEMO
# ---------------------------------------------------------------------------
def time_algorithm(fn: Callable, *args) -> float:
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start


def growth_demo() -> None:
    """Show that wall-clock time tracks the predicted growth function."""
    print(f"{'n':>8} | {'insertion (s)':>14} | {'merge (s)':>10} | "
          f"{'ins/merge':>9}")
    print("-" * 55)
    for n in (1_000, 2_000, 4_000, 8_000):
        # Worst case for insertion sort: reverse-sorted input
        worst = list(range(n, 0, -1))
        t_ins = time_algorithm(insertion_sort, worst[:])
        t_mrg = time_algorithm(merge_sort, worst[:])
        print(f"{n:>8} | {t_ins:>14.4f} | {t_mrg:>10.4f} | "
              f"{(t_ins / max(t_mrg, 1e-9)):>9.1f}x")
    print("\nDoubling n should roughly 4x insertion sort and ~2.2x merge sort.")


# ---------------------------------------------------------------------------
# 8. RACE-CONDITION DEMONSTRATION
# ---------------------------------------------------------------------------
# Module notes describe a counter being read, incremented, and written
# without synchronization. Here is the actual failure in Python.
#
# CPython's GIL provides *some* protection, but += on a shared mutable
# attribute is NOT atomic; it decomposes to LOAD / ADD / STORE just like
# the pseudocode in the notes.
class UnsafeCounter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # Split the read-modify-write so a thread switch *will* occur between
        # the read and the write. Mirrors the notes' pseudocode:
        #     read counter ; counter = counter + 1 ; write counter
        current = self.value
        # Yield the GIL/scheduler so another thread can interleave here.
        time.sleep(0)
        self.value = current + 1


class SafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            current = self.value
            time.sleep(0)
            self.value = current + 1


def race_condition_demo(iterations: int = 10_000,
                        threads: int = 4) -> None:
    for counter_class in (UnsafeCounter, SafeCounter):
        counter = counter_class()

        def worker():
            for _ in range(iterations):
                counter.increment()

        thread_pool = [threading.Thread(target=worker) for _ in range(threads)]
        for t in thread_pool: t.start()
        for t in thread_pool: t.join()

        expected = iterations * threads
        actual = counter.value
        print(f"{counter_class.__name__:>14}: expected {expected:>8}, "
              f"got {actual:>8}, lost {expected - actual:>6}")


# ---------------------------------------------------------------------------
# DEMO HARNESS
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Linear vs Binary Search ===")
    data_sorted = list(range(1, 1_000_001))     # 1..1,000,000
    target = 987_654
    idx, cmp_lin = linear_search(data_sorted, target)
    print(f"Linear search comparisons : {cmp_lin:,}  (expected ~{target:,})")
    idx, cmp_bin = binary_search_iterative(data_sorted, target)
    print(f"Binary search comparisons : {cmp_bin:,}  "
          f"(expected ~log2 n = {math.log2(len(data_sorted)):.1f})")

    print("\n=== Insertion Sort: best vs worst case ===")
    sorted_input = list(range(1, 1001))
    reverse_input = list(range(1000, 0, -1))
    _ = insertion_sort(sorted_input[:])
    print(f"Sorted (best)   comparisons : "
          f"{insertion_sort(sorted_input[:]):>7,}   ≈ n - 1 = 999")
    print(f"Reversed (worst) comparisons: "
          f"{insertion_sort(reverse_input[:]):>7,}   ≈ n(n-1)/2 = "
          f"{1000 * 999 // 2:,}")

    print("\n=== Merge Sort ===")
    arr = random.sample(range(10_000), 1_000)
    sorted_arr, cmp_merge = merge_sort(arr)
    print(f"Merge sort comparisons on n=1000: {cmp_merge:,}  "
          f"(n log2 n ≈ {int(1000 * math.log2(1000)):,})")
    assert sorted_arr == sorted(arr)

    print("\n=== Towers of Hanoi ===")
    for n in (1, 3, 5, 10):
        moves = towers_of_hanoi(n)
        print(f"n = {n:>2}: {len(moves):>5,} moves   (2^n - 1 = "
              f"{2 ** n - 1})")

    print("\n=== Recursive vs Iterative Factorial ===")
    print(f"factorial_iterative(10) = {factorial_iterative(10)}")
    print(f"factorial_recursive(10) = {factorial_recursive(10)}")
    print("(Recursive version uses Θ(n) stack — try n = 5000 to see the limit.)")

    print("\n=== Empirical Growth Demo ===")
    growth_demo()

    print("\n=== Race Condition Demo ===")
    race_condition_demo()
