"""
Why Union-by-Rank + Path Compression Matter  (CSC310 Module 6A - Disjoint Sets)
==============================================================================

A naive disjoint-set forest can degenerate into a chain so FIND-SET becomes 
O(n); union by rank keeps height <= log2(n)+1, and adding path compression 
drops the amortized cost per operation to O(alpha(n)) - effectively
constant (alpha(n) < 4 for any realistic input).
"""


class NaiveDSU:
    """No union by rank, no path compression -- can degenerate into a chain."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.hops = 0

    def find(self, x):
        while self.parent[x] != x:
            self.hops += 1          # count each pointer we follow
            x = self.parent[x]
        return x

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


class OptimizedDSU:
    """Union by rank + path compression."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.hops = 0

    def find(self, x):
        root = x
        while self.parent[root] != root:
            self.hops += 1
            root = self.parent[root]
        while self.parent[x] != root:   # path compression: point everyone at root
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] > self.rank[ry]:
            rx, ry = ry, rx
        self.parent[rx] = ry
        if self.rank[rx] == self.rank[ry]:
            self.rank[ry] += 1


def measure(dsu_class, n):
    """Build one set with a worst-case union order, then FIND every element."""
    dsu = dsu_class(n)
    for i in range(1, n):
        dsu.union(i - 1, i)         # chain-style unions (worst case for naive)
    dsu.hops = 0                    # count only the FIND-SET sweep
    for i in range(n):
        dsu.find(i)
    return dsu.hops / n             # average pointer hops per FIND-SET


def main():
    print("Average pointer hops per FIND-SET after n-1 chain unions:")
    print(f"{'n':>8}  {'naive':>12}  {'union+rank+compress':>22}")
    print("-" * 46)
    for n in (16, 64, 256, 1024, 4096):
        print(f"{n:>8}  {measure(NaiveDSU, n):>12.1f}  "
              f"{measure(OptimizedDSU, n):>22.2f}")
    print()
    print("Naive grows roughly linearly with n (degenerate chain), while the")
    print("optimized forest stays near 1 hop -- the near-constant alpha(n) behavior.")


if __name__ == "__main__":
    main()
