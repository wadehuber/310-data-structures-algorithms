# Disjoint Sets (Union-Find)

Code examples for **Module 6A — Disjoint Sets** (CLRS Ch. 19). 
A disjoint-set structure maintains a partition of elements into
non-overlapping sets and supports three operations: `MAKE-SET(x)`,
`FIND-SET(x)` (which set's representative?), and `UNION(x, y)` (merge two sets).
It is the engine behind Kruskal's MST and dynamic-connectivity problems.

> The Python file is a complexity *measurement*, not the operations.

## Examples

| File | Language | What it shows |
|------|----------|---------------|
| [`uf_complexity.py`](uf_complexity.py) | Python | Instruments FIND-SET to count pointer hops; naive forest vs. union-by-rank + path compression as n grows. |
| [`union_find.go`](union_find.go) | Go | Array-based forest, rank + path compression, `Connected` query. |
| [`union_find.scm`](union_find.scm) | Scheme | Two-vector (`parent`, `rank`) forest with recursive path compression. |
| [`union_find.pl`](union_find.pl) | Prolog | Dynamic `parent/2` and `rank/2` facts; compression via retract/assert. |

The three implementations run the same demo (elements 0–6; unions (0,1), (2,3),
(1,3), (4,5)) and print the same partition:

```text
Sets: {0, 1, 2, 3} {4, 5} {6}
connected(0,3)? true
connected(0,4)? false
```

## The two optimizations 

- **Union by rank** — attach the shorter tree under the taller one; equal ranks
  bump the new root's rank by 1. Keeps height ≤ log₂(n)+1.
- **Path compression** — during `FIND-SET`, repoint every node on the path
  directly at the root, flattening the tree.

Together they give an amortized cost of **O(α(n))** per operation, where the
inverse Ackermann function α(n) < 4 for any realistic input — effectively
constant. `uf_complexity.py` makes the difference visible:

```text
       n         naive     union+rank+compress
      16           7.5                    0.94
    4096        2047.5                    1.00
```

## Running

```bash
python3 uf_complexity.py
go run union_find.go                       # Go
guile union_find.scm                       # Scheme (GNU Guile)
swipl -g main -t halt union_find.pl        # Prolog (SWI) 
```

## Where each ties back to the notes

- *Core Operations (MAKE-SET / FIND-SET / UNION)* → `union_find.{go,scm,pl}`
- *Union by rank & Path compression* → all implementations + `uf_complexity.py`
- *Disjoint-Set Forests / degenerate chains* → `uf_complexity.py`
