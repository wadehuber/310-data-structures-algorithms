"""
Hash Function Quality Comparison  (CSC310 Module 4B - Hashing)
============================================================

Two quality measures from the notes:
  - Distribution: collisions / empty slots / longest bucket when n keys are
    hashed into a prime-sized table.  A good hash spreads keys evenly.
  - Avalanche: when one input bit changes, about half the output bits should
    flip.  A weak hash barely changes its output.

Strategies (division, multiplication, folding, mid-square) are from the notes'
"Hashing Strategies" section; "first digit" is the deliberately poor one.
"""
import random
import statistics


# ---------- table-index strategies: map integer key -> [0, m) ----------
A = 0.6180339887  # (sqrt(5)-1)/2, Knuth's multiplicative constant

def h_division(k, m):
    return k % m

def h_multiplication(k, m):
    return int(m * ((k * A) % 1.0))

def h_shift_fold(k, m):
    s = str(k)
    total = sum(int(s[i:i + 2]) for i in range(0, len(s), 2))  # 2-digit groups
    return total % m

def h_mid_square(k, m):
    sq = str(k * k)
    mid = sq[len(sq) // 2 - 1: len(sq) // 2 + 2] or sq      # middle ~3 digits
    return int(mid) % m

def h_first_digit(k, m):  # deliberately poor: only the leading digit
    return int(str(k)[0]) % m


STRATEGIES = [
    ("division", h_division),
    ("multiplication", h_multiplication),
    ("shift folding", h_shift_fold),
    ("mid-square", h_mid_square),
    ("first digit (poor)", h_first_digit),
]


def distribution_report(keys, m):
    # birthday-style expected collisions for an ideal uniform hash, as a baseline
    n = len(keys)
    expected = n - m * (1 - ((m - 1) / m) ** n)
    print(f"Distribution of {n} keys into a table of size {m} "
          f"(ideal uniform hash collides ~{expected:.0f} times):")
    print(f"  {'strategy':<20}{'used':>6}{'empty':>7}{'max load':>10}{'collisions':>12}")
    print("  " + "-" * 55)
    for name, h in STRATEGIES:
        buckets = [0] * m
        for k in keys:
            buckets[h(k, m)] += 1
        used = sum(1 for b in buckets if b)
        print(f"  {name:<20}{used:>6}{m - used:>7}{max(buckets):>10}"
              f"{len(keys) - used:>12}")


# ---------- 32-bit hashes for the avalanche test ----------
MASK = 0xFFFFFFFF

def mix32(k):                       # good: multiply + xorshift (avalanches well)
    k = (k * 2654435761) & MASK
    k ^= k >> 16
    k = (k * 2246822519) & MASK
    k ^= k >> 13
    return k & MASK

def weak32(k):                      # poor: keep low bits only
    return (k * 3) & MASK


def avalanche(hfun, trials=4000):
    """Average fraction of the 32 output bits that flip when one input bit flips."""
    rng = random.Random(0)
    total_flip = 0
    for _ in range(trials):
        k = rng.getrandbits(32)
        base = hfun(k)
        bit = rng.randrange(32)
        diff = base ^ hfun(k ^ (1 << bit))
        total_flip += bin(diff).count("1")
    return total_flip / trials / 32.0


def main():
    rng = random.Random(7)
    keys = [rng.randint(100000, 999999) for _ in range(80)]   # 80 6-digit keys
    m = 97                                                    # prime table size

    distribution_report(keys, m)
    print()
    print("Avalanche (fraction of 32 output bits that flip per input-bit flip;")
    print("a good hash is near 0.50):")
    print(f"  mix32 (good multiply + xorshift): {avalanche(mix32):.3f}")
    print(f"  weak32 (low bits only)          : {avalanche(weak32):.3f}")


if __name__ == "__main__":
    main()
