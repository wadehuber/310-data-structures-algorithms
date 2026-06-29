# Spanning Trees

Code examples from **Module 9 — Spanning Trees** notes (CLRS Ch. 21;
 Java Foundations Ch. 24). A spanning tree connects all |V| vertices with
exactly |V|−1 edges and no cycles; a **minimum spanning tree (MST)** does
so with the least total edge weight. The greedy MST algorithms are proved
correct by the **cut property** (the lightest edge crossing any cut is
safe) and the **cycle property** (the heaviest edge on any cycle is never used).

## Examples

| Topic | Language(s) | Notes |
|-------|-------------|-------|
| Brute-force MST + cut/cycle properties | Python | Enumerates all 55 spanning trees of the demo graph, confirms min weight **14**, and demonstrates the cut and cycle properties. |
| Kruskal's algorithm | Scheme | **Different graph**. Edge-sorted + union-find. Total weight 14. |
| Prim's algorithm | Go | **Different graph**. Grows one tree from a start vertex. Total weight 14. |

All three operate on the same 6-vertex graph, so Kruskal, Prim, and the
exhaustive search all arrive at total weight 14 by different routes.

## What each shows

- **Brute-force MST** — by enumerating every spanning tree it shows *what* the
  optimum is (and how many spanning trees exist), then verifies the cut property
  (lightest crossing edge is in the MST) and cycle property (heaviest cycle edge
  is not). This is why the greedy algorithms are correct — and why exhaustive
  search is impractical beyond tiny graphs.
- **Kruskal** — considers edges in increasing weight, adding one only if it
  joins two different components (union-find prevents cycles).
- **Prim** — grows a single tree, always taking the cheapest edge leaving it.

## Running

```bash
python3 mst_bruteforce.py

# Kruskal (GNU Guile)
guile kruskal.scm

# Prim
go run prim.go
```

## Where each ties back to the notes

- *Cut Property / Cycle Property* → `mst_bruteforce.py`
- *Kruskal's Algorithm* (edge-sorted, union-find) → `kruskal.scm`
- *Prim's Algorithm* (growing tree, cheapest outgoing edge) → `prim.go`
