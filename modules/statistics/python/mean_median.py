"""
Mean vs. Median: A Robustness Illustration
-------------------------------------------
A demonstration of the "Robust Statistics" idea from the "Medians & Order
Statistics" notes:

    Mean is sensitive to values.  Median is sensitive only to order.

This script computes both, then injects a single extreme value and recomputes,
so you can see the mean lurch toward the outlier while the median barely moves.
That is the whole point of calling the median *robust*: a small fraction of
extreme values cannot significantly change it.

(Computing the median here uses Python's sort for clarity.  As the notes
explain -- and as select_medians.py / randselect.py show -- the median can
actually be found in Theta(n) time without fully sorting.)
"""


def mean(data):
    """Arithmetic mean: sum of values divided by count. Uses every value."""
    return sum(data) / len(data)


def median(data):
    """
    Middle value after ordering.  Depends only on relative order, not on
    how large the extreme values are.
    """
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def report(label, data):
    print(f"{label}")
    print(f"  data:   {data}")
    print(f"  mean:   {mean(data):.2f}")
    print(f"  median: {median(data):.2f}")
    print()


def main():
    # Server response times in milliseconds: tightly clustered, no outlier.
    clean = [102, 98, 105, 99, 101, 103, 100, 97, 104]
    report("Clean readings:", clean)

    # One request hit a stall (a 4000 ms spike). Same data plus one outlier.
    with_outlier = clean + [4000]
    report("With one extreme outlier added:", with_outlier)

    base_mean, base_median = mean(clean), median(clean)
    out_mean, out_median = mean(with_outlier), median(with_outlier)
    print("Effect of the single outlier:")
    print(f"  mean   moved by {out_mean - base_mean:8.2f} ms  (chases the outlier)")
    print(f"  median moved by {out_median - base_median:8.2f} ms  (stays put -> robust)")


if __name__ == "__main__":
    main()
