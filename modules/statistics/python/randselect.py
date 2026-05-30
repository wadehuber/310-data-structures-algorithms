import random

def randomized_partition(A, p, r):
    """
    Chooses a random pivot, swaps it with A[r], then partitions the array
    around the pivot.  
    Returns the final pivot index.
    """
    pivot_index = random.randint(p, r)
    A[pivot_index], A[r] = A[r], A[pivot_index]
    return partition(A, p, r)


def partition(A, p, r):
    """
    Standard Lomuto partition scheme.
    """
    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_select(A, i):
    """
    Returns the i-th smallest element of A
    """
    return randomized_select_range(A, 0, len(A) - 1, i)

def randomized_select_range(A, p, r, i):
    """
    Returns the i-th smallest element of A[p..r]
    i is 1-based 
    """
    if p == r:
        return A[p]

    q = randomized_partition(A, p, r)
    k = q - p + 1  # rank of pivot within subarray

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select_range(A, p, q - 1, i)
    else:
        return randomized_select_range(A, q + 1, r, i - k)


def main():
    A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    i = 5  # Find the 5th smallest element

    print("Original array:", A)

    result = randomized_select(A, i)

    print(f"{i}th smallest element:", result)

    # Optional verification
    sorted_A = sorted(A)
    print("Sorted array:", sorted_A)
    print(f"Check: {sorted_A[i - 1]}")


if __name__ == "__main__":
    main()
