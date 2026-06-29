# Dynamic Programming

Code examples for **Module 11 — Dynamic Programming** (CLRS Ch. 14).
Dynamic programming turns exponential recursion into polynomial
time by solving each distinct overlapping subproblem once and reusing the
result. Every example here pairs a **value table** (the optimal cost) with a
**choice table** (how to rebuild the actual solution) — the central pattern from
the notes.

## Examples

- **Optimal BST** — minimizing *expected* search cost when keys have access
  probabilities. Demonstrates a Theta(n^3) chain-style DP, the value-vs-choice
  table split, and reconstructing the optimal tree from the `root` table.
- **Rod cutting** — the canonical 1-D DP. `r[j]` is the best revenue for length
  `j`; the `s[j]` choice table recovers the actual set of cuts.
- **Matrix chain** — the canonical 2-D "fill by increasing chain length" DP.
  Associativity changes the multiplication cost; the `s[i][j]` table recovers the
  optimal parenthesization.

## Running the code

```bash
# Optimal BST
python3 optimal_bst.py
javac OptimalBST.java && java OptimalBST

# Rod cutting (R5RS Scheme, e.g. GNU Guile)
#  Also tested in DrRacket
guile rod_cutting.scm

# Matrix chain
go run matrix_chain.go
```

## Where each ties back to the notes

- *Rod Cutting* (bottom-up + reconstruction) -> `rod_cutting.scm`
- *Matrix Chain Multiplication* (`m`/`s` tables, fill by chain length) -> `matrix_chain.go`
- *Optimal Binary Search Trees* (the advanced example) -> `optimal_bst.py`, `OptimalBST.java`
- *Value tables vs. choice tables* -> every example keeps both
