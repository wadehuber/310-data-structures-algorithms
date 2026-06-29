# Shortest Paths

Code examples from **Module 10 — Shortest Paths** (CLRS Ch. 22–23; 
Java Foundations Ch. 24). Every algorithm here is built on **relaxation**:
if a known route to `u` plus the edge `(u, v)` beats the current
estimate `d[v]`, update `d[v]` and record `u` as `v`'s predecessor. The
algorithms differ only in the order they relax edges.

## Examples

| Algorithm | When to use it | Language | Graph |
|-----------|----------------|----------|-------|
| Dijkstra | Nonnegative weights, single source | Go | CLRS Fig. 24.6 → d = 0,8,9,5,7 |
| Bellman-Ford | Negative edges; detects negative cycles | Prolog | CLRS Fig. 24.4 → d = 0,2,4,7,−2 |
| Floyd-Warshall | All-pairs, dense graphs, negative edges OK | Scheme | CLRS Fig. 25.1 (full distance matrix) |

## What each shows

- **Dijkstra** — greedy: settle the closest unsettled vertex, then relax its
  edges. Safe only because nonnegative weights mean a settled vertex can never be
  improved later.
- **Bellman-Ford** — relax *every* edge |V|−1 times; this tolerates negative
  edges, and one extra pass detects a negative-weight cycle. Written
  declaratively in Prolog, distances carried in a `V-D` list (no mutable arrays).
- **Floyd-Warshall** — the Θ(n³) dynamic program: allow each vertex in turn as an
  intermediate and keep the cheaper of "skip k" vs. "go through k."

The notes' decision guide: DAG → DAG-shortest-paths; nonnegative + sparse →
Dijkstra; negative + dense → Floyd-Warshall; negative + sparse → Johnson's;
"something that always works" → Bellman-Ford.

## Running

```bash
# Dijkstra
go run dijkstra.go

# Bellman-Ford (SWI-Prolog)
swipl -g main -t halt bellman_ford.pl

# Floyd-Warshall (GNU Guile)
guile floyd_warshall.scm
```

## Where each ties back to the notes

- *Relaxation* → the core update in all three files
- *Dijkstra's Algorithm* → `dijkstra.go`
- *Bellman-Ford Algorithm* (+ negative-cycle detection) → `bellman_ford.pl`
- *Floyd-Warshall (all-pairs DP)* → `floyd_warshall.scm`
