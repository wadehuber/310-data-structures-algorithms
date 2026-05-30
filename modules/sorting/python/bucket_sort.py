"""
Bucket Sort
-----------
A demonstration of bucket sort from the "Sorting in Linear Time" notes.

Bucket sort assumes the input is real numbers uniformly distributed over
[0, 1).  It divides that range into n equal buckets, drops each element
into the bucket for its range, sorts each bucket with a simple method
(insertion sort works well because buckets stay small), and concatenates.

Under the uniform assumption each bucket holds roughly a constant number of
elements, giving O(n) expected time.

This example sorts uniform [0, 1) scores -- the kind of normalized
confidence values the notes mention -- and prints the bucket contents so
you can see the distribute-then-concatenate structure.
"""


def insertion_sort(values):
    """Plain insertion sort; fast on the short lists inside each bucket."""
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    return values


def bucket_sort(A, show_buckets=False):
    """
    Return a sorted copy of A, where every element is in [0, 1).

    Uses n buckets so that element x lands in bucket floor(n * x).
    """
    n = len(A)
    if n == 0:
        return []

    buckets = [[] for _ in range(n)]

    # Distribute: bucket index scales with the value because input is in [0, 1).
    for x in A:
        index = int(n * x)
        if index == n:          # guard the x == 1.0 edge if it ever appears
            index = n - 1
        buckets[index].append(x)

    # Sort each bucket, then concatenate in order.
    result = []
    for i, bucket in enumerate(buckets):
        insertion_sort(bucket)
        if show_buckets:
            print(f"  bucket {i} [{i/n:.2f}, {(i+1)/n:.2f}): {bucket}")
        result.extend(bucket)

    return result


def main():
    scores = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

    print("Input scores:", scores)
    print("Buckets:")
    result = bucket_sort(scores, show_buckets=True)
    print("Bucket sorted: ", result)
    print("Python sorted():", sorted(scores))


if __name__ == "__main__":
    main()
