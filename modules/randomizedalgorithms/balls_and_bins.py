"""
Balls and Bins  (CSC310 Module 13 - Randomized Algorithms)
==========================================================

Throw m balls independently and uniformly into n bins.  The expected load per
bin is m/n, but the interesting quantity is the MAXIMUM load.  When m = n, the
heaviest bin holds about ln n / ln ln n balls with high probability -- much more
than the average of 1.  This is the "max load" result used to reason about hash
collisions.  This program estimates it by simulation and compares to the average.
"""
import random
import math


def simulate_max_load(n_balls, n_bins, trials):
    total_max = 0
    total_empty = 0
    for _ in range(trials):
        bins = [0] * n_bins
        for _ in range(n_balls):
            bins[random.randrange(n_bins)] += 1
        total_max += max(bins)
        total_empty += bins.count(0)
    return total_max / trials, total_empty / trials


def main():
    trials = 2000
    print(f"Averaged over {trials} trials, with m = n balls into n bins:\n")
    print(f"{'n':>8}  {'avg load':>9}  {'avg max load':>13}  "
          f"{'ln n / ln ln n':>15}  {'avg empty bins':>15}")
    print("-" * 70)
    for n in (10, 100, 1000, 10000):
        avg_max, avg_empty = simulate_max_load(n, n, trials)
        # theoretical guideline for the max load when m = n (n large)
        guide = (math.log(n) / math.log(math.log(n))) if n >= 3 else float("nan")
        print(f"{n:>8}  {1.0:>9.2f}  {avg_max:>13.2f}  {guide:>15.2f}  "
              f"{avg_empty:>15.1f}")
    print()
    print("Average load is always 1, but the busiest bin grows like")
    print("ln n / ln ln n -- the reason a hash table's worst bucket is")
    print("longer than the average bucket.")
    print()
    # Empty-bin check: expected fraction empty ~ 1/e when m = n.
    print(f"Expected empty fraction when m = n is about 1/e = {1/math.e:.3f}")


if __name__ == "__main__":
    main()
