"""
Randomized Quicksort
 
A divide-and-conquer sorting algorithm that randomly selects a pivot element.
The algorithm partitions the array into elements less than, equal to, and
greater than the pivot, then recursively sorts the smaller partitions.
 
By randomly selecting the pivot, the algorithm avoids worst-case O(n^2)
behavior on already-sorted input while maintaining expected O(n log n) time.
 
Expected Time Complexity: O(n log n)
Worst Case Time Complexity: O(n^2) (rare with random pivot selection)
Space Complexity: O(log n) average (recursion depth)
 
Based on CLRS Chapter 7 - Quicksort
"""

import random

def randomized_quicksort(arr):
    """
    Sort an array using randomized quicksort.
 
    Args:
        arr: List of comparable elements to sort
 
    Returns:
        Sorted list in ascending order
    """

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Demo
data = [5, 1, 8, 3, 7, 2, 4, 6]
print(f"Original data: {data}")
new_data = randomized_quicksort(data)
print(f"Sorted data: {new_data}")
