# Graph Search & Traversal

Code examples from **Module 7 — Graph Algorithms** (CLRS Ch. 20; 
Java Foundations Ch. 24). Every graph search is built on a
traversal of the reachable vertices; the difference is what you
compute along the way (distances, timestamps, components, orderings).

## Examples

| Topic | Status | Language(s) | Notes |
|-------|--------|-------------|-------|
| Topological sort | Python, Java | DFS finish-order ordering of a DAG + cycle detection. CLRS "getting dressed" graph. |
| Strongly connected components (Kosaraju) | Python, C++ | Two-pass DFS + transpose. CLRS Fig. 22.9 → components {a,b,e}, {c,d}, {f,g}, {h}. |
| DFS edge classification | Python | Tree / back / forward / cross edges from discovery & finish times; back edge ⇔ cycle. |
| BFS and DFS traversal | Prolog | **Different graph** (vertices p..u). |

Topological sort and SCC use DFS internally, but they are distinct algorithms
that no assignment asks for; the standalone BFS/DFS traversal that Project 3
targets is kept in Prolog only.

## What each shows

- **Topological sort** — orders a DAG so every edge points forward; the DFS
  method prepends each vertex as it finishes. A back edge means no ordering
  exists.
- **Strongly connected components** — Kosaraju's two DFS passes (on G, then on
  the transpose in decreasing finish order) recover the maximal mutually
  reachable vertex sets.
- **Edge classification** — the discovery/finish timestamps from one DFS label
  every edge, and the presence of a back edge is exactly a cycle test.
- **BFS / DFS** — the two fundamental traversals: BFS by queue (level order),
  DFS by recursion (deep first).

## Running

```bash
python3 topological_sort.py
javac TopologicalSort.java && java TopologicalSort

python3 scc_kosaraju.py
g++ -std=c++17 -O2 scc_kosaraju.cpp -o scc_kosaraju && ./scc_kosaraju

python3 edge_classification.py

# BFS/DFS (SWI-Prolog)
swipl -g main -t halt graph_search.pl
# SICStus:  sicstus -l graph_search.pl --goal "main."
```

## Where each ties back to the notes

- *Breadth-First / Depth-First Traversal* → `graph_search.pl`
- *Edge Classification in DFS* → `edge_classification.py`
- *Topological Sort* → `topological_sort.py`, `TopologicalSort.java`
- *Strongly Connected Components (Kosaraju)* → `scc_kosaraju.py`, `scc_kosaraju.cpp`
