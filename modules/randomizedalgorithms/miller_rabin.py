"""
Miller-Rabin Primality Test  (CSC310 Module 13 - Randomized Algorithms)
======================================================================

Miller-Rabin is a MONTE CARLO algorithm: bounded running time, with a small
probability of error that shrinks with each extra random witness.  Using a fixed
set of small bases makes it *deterministic and correct* for all 64-bit integers.

The contrast with the Fermat test: a Carmichael number (e.g. 561 = 3*11*17)
satisfies a^(n-1) = 1 (mod n) for EVERY base a coprime to n.  So every coprime
base is a "Fermat liar" -- if the Fermat test never happens to pick a base that
shares a factor with n, it wrongly reports "prime."  Miller-Rabin uses the extra
square-root check, so these same numbers are caught.
"""
from math import gcd

# These bases make Miller-Rabin deterministic for all n < 3.3 * 10^24.
DETERMINISTIC_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_probable_prime(n, witnesses=None):
    if n < 2:
        return False
    for p in (2, 3):
        if n == p:
            return True
        if n % p == 0:
            return False

    d, r = n - 1, 0            # write n - 1 = d * 2^r with d odd
    while d % 2 == 0:
        d //= 2
        r += 1

    if witnesses is None:
        witnesses = [a for a in DETERMINISTIC_BASES if a < n]

    for a in witnesses:
        x = pow(a, d, n)        # fast modular exponentiation
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False        # a is a witness: n is definitely composite
    return True                 # probably prime (certain for the fixed bases)


def fermat_liar_rate(n):
    """Fraction of bases coprime to n that satisfy a^(n-1) = 1 (mod n).
    For a prime this is 100%; for a Carmichael number it is also 100% (that is
    the trap); for a typical composite it is small."""
    coprime = liars = 0
    for a in range(2, n - 1):
        if gcd(a, n) == 1:
            coprime += 1
            if pow(a, n - 1, n) == 1:
                liars += 1
    return liars, coprime


def main():
    samples = [561, 1105, 1729, 997, 7919, 9973]
    carmichael = {561, 1105, 1729}
    print(f"{'n':>8}  {'Miller-Rabin':>12}  {'Fermat liars (coprime bases)':>30}")
    print("-" * 56)
    for n in samples:
        mr = "prime" if is_probable_prime(n) else "composite"
        liars, coprime = fermat_liar_rate(n)
        rate = f"{liars}/{coprime} = {100*liars/coprime:.0f}%"
        note = "  <- Carmichael" if n in carmichael else ""
        print(f"{n:>8}  {mr:>12}  {rate:>30}{note}")
    print()
    print("For the Carmichael numbers, 100% of coprime bases are Fermat liars,")
    print("so the Fermat test reports 'prime' unless it stumbles onto a base that")
    print("shares a factor with n.  Miller-Rabin reports them as composite.")
    print()
    # Big prime to show it scales: a Mersenne prime.
    big = (1 << 61) - 1
    print(f"Miller-Rabin({big}) = "
          f"{'prime' if is_probable_prime(big) else 'composite'}  (2^61 - 1)")


if __name__ == "__main__":
    main()
