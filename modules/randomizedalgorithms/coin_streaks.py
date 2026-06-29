"""
Streaks in Coin Flips  (CSC310 Module 13 - Randomized Algorithms)
================================================================

Flip a fair coin n times.  How long is the longest run of consecutive heads?
The notes state the longest streak in n fair flips is on the order of log2(n),
not linear.  This program estimates the average longest streak by simulation and
compares it to log2(n).
"""
import random
import math


def longest_head_run(n):
    best = current = 0
    for _ in range(n):
        if random.random() < 0.5:        # heads
            current += 1
            best = max(best, current)
        else:                            # tails resets the run
            current = 0
    return best


def main():
    trials = 5000
    print(f"Averaged over {trials} trials of n fair coin flips:\n")
    print(f"{'n':>8}  {'avg longest head run':>22}  {'log2(n)':>10}")
    print("-" * 46)
    for n in (16, 64, 256, 1024, 4096):
        avg = sum(longest_head_run(n) for _ in range(trials)) / trials
        print(f"{n:>8}  {avg:>22.2f}  {math.log2(n):>10.2f}")
    print()
    print("The longest run tracks log2(n): each time n quadruples, the longest")
    print("streak grows by about 2 -- logarithmic, not linear, growth.")


if __name__ == "__main__":
    main()
