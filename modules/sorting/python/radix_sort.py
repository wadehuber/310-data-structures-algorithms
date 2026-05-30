"""
Radix Sort (LSD)
----------------
A demonstration of least-significant-digit radix sort from the
"Sorting in Linear Time" notes.

Radix sort extends counting sort to multi-digit numbers by sorting one
digit at a time, from least significant to most significant.  Each pass
uses a *stable* counting sort as its subroutine, so the ordering achieved
by earlier (lower) digits survives later passes.

For d-digit numbers in base r it runs in Theta(d * (n + r)) time -- linear
in the input when the number of digits d is small or constant.

This example sorts fixed-width integer keys (think hashed feature ids or
quantized values) in base 10 so you can print the array after each digit
pass and watch it converge.
"""


def counting_sort_by_digit(A, exp, base=10):
    """
    Stable counting sort of A using the digit selected by `exp`.

    `exp` is a power of `base`: exp=1 sorts by the ones digit, exp=10 by the
    tens digit, and so on.  Stability here is what makes the multi-pass
    radix sort correct.
    """
    n = len(A)
    C = [0] * base
    B = [0] * n

    # Count occurrences of each digit value (0..base-1).
    for value in A:
        digit = (value // exp) % base
        C[digit] += 1

    # Cumulative sums -> ending positions.
    for d in range(1, base):
        C[d] += C[d - 1]

    # Place right-to-left to preserve stability.
    for j in range(n - 1, -1, -1):
        digit = (A[j] // exp) % base
        C[digit] -= 1
        B[C[digit]] = A[j]

    return B


def radix_sort(A, base=10, trace=False):
    """
    Return a sorted copy of A (non-negative integers), one digit pass at a
    time.  Set trace=True to print the array after each pass.
    """
    if not A:
        return []

    result = list(A)
    max_value = max(result)

    exp = 1
    while max_value // exp > 0:
        result = counting_sort_by_digit(result, exp, base)
        if trace:
            place = "ones" if exp == 1 else f"{exp}s"
            print(f"  after {place:>6} digit: {result}")
        exp *= base

    return result


def main():
    keys = [329, 457, 657, 839, 436, 720, 355, 8, 90, 3]

    print("Input keys:", keys)
    print("Radix sort passes (LSD -> MSD):")
    result = radix_sort(keys, trace=True)
    print("Radix sorted:  ", result)
    print("Python sorted():", sorted(keys))


if __name__ == "__main__":
    main()
