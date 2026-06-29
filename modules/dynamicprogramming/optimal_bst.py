"""
Optimal Binary Search Tree  (CSC310 Module 11 - Dynamic Programming)
====================================================================

Problem:  Given keys k1 < k2 < ... < kn with search probabilities p[i], and
"dummy" keys d0..dn for unsuccessful searches with probabilities q[i], build a
binary search tree that minimizes the EXPECTED search cost
        sum over nodes of (depth + 1) * probability.

This is the CLRS algorithm (Sec. 15.5 / 3e):
    e[i][j] = expected cost of an optimal BST over keys k_i..k_j
    w[i][j] = total probability mass in that range (lets us add the +1 per level)
    root[i][j] = key index chosen as the root of that subtree (the CHOICE table)

Time  : Theta(n^3)        Space : Theta(n^2)
"""

INF = float("inf")


def optimal_bst(p, q):
    """p is 1-indexed (p[1..n]); q is 0-indexed (q[0..n]). Returns (e, root)."""
    n = len(p) - 1
    # e[i][j] valid for 1 <= i <= n+1, i-1 <= j <= n
    e = [[0.0] * (n + 1) for _ in range(n + 2)]
    w = [[0.0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * (n + 1) for _ in range(n + 1)]

    # base case: empty subtree between k_{i-1} and k_i is just dummy d_{i-1}
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for length in range(1, n + 1):            # subtree size
        for i in range(1, n - length + 2):
            j = i + length - 1
            e[i][j] = INF
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j + 1):         # try every key as the root
                cost = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r
    return e, root


def build_structure(root, i, j, lines, depth=0, label="root"):
    """Walk the choice table to describe the optimal tree."""
    if i > j:
        lines.append("  " * depth + f"{label}: d{j}  (dummy leaf)")
        return
    r = root[i][j]
    lines.append("  " * depth + f"{label}: k{r}")
    build_structure(root, i, r - 1, lines, depth + 1, "left ")
    build_structure(root, r + 1, j, lines, depth + 1, "right")


def main():
    # Classic CLRS instance (answer is known: expected cost = 2.75).
    p = [None, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    n = len(p) - 1

    e, root = optimal_bst(p, q)

    print("Keys k1..k5 with probabilities:")
    print("  p =", p[1:])
    print("  q =", q)
    print()
    print(f"Expected cost of the optimal BST: {e[1][n]:.2f}")
    print(f"Root of the whole tree           : k{root[1][n]}")
    print()
    print("Optimal tree structure:")
    lines = []
    build_structure(root, 1, n, lines)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
