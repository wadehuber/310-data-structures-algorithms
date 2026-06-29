"""
Collision Resolution Compared  (CSC310 Module 4B - Hashing)
==========================================================

Methods:
  - Chaining: each slot holds a list.        Successful search ~ 1 + alpha/2.
  - Open addressing (all keys in the array), probe sequences:
      Linear:    h(k,i) = (h(k) + i) mod m            -> primary clustering
      Quadratic: h(k,i) = (h(k) + i^2) mod m          -> secondary clustering
      Double:    h(k,i) = (h1(k) + i*h2(k)) mod m     -> best in practice
    Successful search ~ (1/alpha) * ln(1/(1-alpha)).

Also demonstrates tombstone deletion (a deleted slot must not stop a search).
"""
import math
import random

M = 101                      # prime table size
EMPTY, DELETED = None, "<del>"


def h1(k): return k % M
def h2(k): return 1 + (k % (M - 1))     # never 0, so double hashing makes progress


# ---------- open addressing ----------
def probe(k, i, scheme):
    if scheme == "linear":    return (h1(k) + i) % M
    if scheme == "quadratic": return (h1(k) + i * i) % M
    return (h1(k) + i * h2(k)) % M       # double

def oa_insert(table, k, scheme):
    for i in range(M):
        slot = probe(k, i, scheme)
        if table[slot] in (EMPTY, DELETED):
            table[slot] = k
            return True
    return False                          # table full / no slot found

def oa_search_probes(table, k, scheme):
    for i in range(M):
        slot = probe(k, i, scheme)
        if table[slot] == k:
            return i + 1                  # number of slots examined
        if table[slot] == EMPTY:
            return i + 1
    return M


def longest_run(table):
    """Longest run of consecutive occupied slots (primary-clustering measure)."""
    best = run = 0
    for cell in table + table:            # wrap-around
        run = run + 1 if cell not in (EMPTY, DELETED) else 0
        best = max(best, run)
    return min(best, sum(1 for c in table if c not in (EMPTY, DELETED)))


def measure_open(keys, scheme):
    table = [EMPTY] * M
    placed = [k for k in keys if oa_insert(table, k, scheme)]
    avg = sum(oa_search_probes(table, k, scheme) for k in placed) / len(placed)
    return avg, longest_run(table)


def measure_chaining(keys):
    table = [[] for _ in range(M)]
    for k in keys:
        table[h1(k)].append(k)
    # successful search cost = position of the key within its chain (1-based)
    total = sum(table[h1(k)].index(k) + 1 for k in keys)
    return total / len(keys)


def main():
    rng = random.Random(7)
    pool = rng.sample(range(100000, 999999), 95)   # distinct keys

    print("Average probes for a successful search vs. load factor:")
    print(f"  {'alpha':>6}{'chaining':>10}{'(1+a/2)':>9}{'linear':>9}"
          f"{'double':>9}{'(theory)':>10}")
    print("  " + "-" * 54)
    for alpha in (0.5, 0.7, 0.9):
        n = int(alpha * M)
        keys = pool[:n]
        chain = measure_chaining(keys)
        lin, _ = measure_open(keys, "linear")
        dbl, _ = measure_open(keys, "double")
        oa_theory = (1 / alpha) * math.log(1 / (1 - alpha))
        print(f"  {alpha:>6.1f}{chain:>10.2f}{1 + alpha/2:>9.2f}"
              f"{lin:>9.2f}{dbl:>9.2f}{oa_theory:>10.2f}")

    print("\nClustering at load factor 0.5 (longest run of occupied slots;")
    print("lower is better -- linear suffers the most):")
    keys = pool[:int(0.5 * M)]
    for scheme in ("linear", "quadratic", "double"):
        _, run = measure_open(keys, scheme)
        print(f"  {scheme:<10}: longest occupied run = {run}")

    print("\nTombstone deletion (linear probing):")
    table = [EMPTY] * M
    for k in (204, 305, 406):              # 204,305,406 all hash near each other
        oa_insert(table, k, "linear")
    # delete the first of the cluster, then confirm the others are still found
    slot = next(i for i in range(M) if table[i] == 204)
    table[slot] = DELETED
    found = oa_search_probes(table, 406, "linear")
    hit = any(table[probe(406, i, "linear")] == 406 for i in range(M))
    print(f"  deleted 204 (tombstone); search for 406 still finds it: {hit} "
          f"(in {found} probes)")


if __name__ == "__main__":
    main()
