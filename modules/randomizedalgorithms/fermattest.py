"""
Fermat Primality Test (Randomized Algorithm)
 
A probabilistic primality test based on Fermat's Little Theorem. For a prime n,
a^(n-1) ≡ 1 (mod n) for all 1 < a < n. This test checks this property for
random values of a. If the test fails for any a, n is definitely composite.
If it passes for all trials, n is probably prime.
 
Time Complexity: O(k log^3 n) where k = number of trials
Space Complexity: O(1)
 
Based on CLRS Chapter 31 - Number-Theoretic Algorithms
"""

import random

def fermat_test(n, trials=5):
    """
    Probabilistic primality test using Fermat's Little Theorem.
 
    Args:
        n: Integer to test for primality
        trials: Number of random tests to perform (higher = higher confidence)
 
    Returns:
        False if n is definitely composite, True if n is probably prime
    """

    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(trials):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True  # probably prime

# Demo
for val in [10, 17, 21, 122, 561, 997]:
    print(f"{val}: {'probably prime' if fermat_test(val) else 'composite'}")
