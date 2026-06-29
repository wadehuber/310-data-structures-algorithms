# Graphs

**Module 6B — Graphs**: graph terminology, directed vs.
undirected vs. weighted graphs, and the two standard representations (adjacency
list and adjacency matrix).

## Videos

- [Introduction to Graphs](https://youtu.be/9zsHWI9vv8g) (8:21): graph terminology and types of graphs (undirected, directed, & weighted).
- [Graph Algorithms](https://youtu.be/UJd3A0nrXg8) (7:59): breadth- and depth-first traversals, spanning trees, and representing graphs with adjacency matrices & adjacency lists.

## Graph data structure 

A simple adjacency-list graph that supports directed and undirected weighted
edges, with `add vertex` and `add edge` operations, neighbor lookup, and edge
weight lookup.

| Language | File | Representation |
|----------|------|----------------|
| Go | [`graph.go`](graph.go) | `map[string][]Edge` + ordered vertex slice |
| Scheme | [`graph.scm`](graph.scm) | record with a hash table of `(neighbor . weight)` lists |
| Prolog | [`graph.pl`](graph.pl) | dynamic `vertex/1` and `adj/3` facts |
| Pascal | [`graph.pas`](graph.pas) | dynamic arrays of vertices and edge records |

All four build the same small weighted graph (an Arizona road network in miles)
and print identical output:

```text
Graph (undirected, weighted) - adjacency list:
  PHX -> MESA(20), TEMPE(11), TUS(116)
  TUS -> MESA(100), PHX(116)
  MESA -> PHX(20), TEMPE(8), TUS(100)
  TEMPE -> MESA(8), PHX(11)
Neighbors of PHX: MESA, TEMPE, TUS
Weight PHX-MESA: 20
```

An undirected edge is stored as two directed edges, which is also how you would
support directed graphs (just add the one direction). Neighbors are printed in
sorted order so the four implementations match regardless of internal ordering.

## Running

```bash
go run graph.go                       # Go
guile graph.scm                       # Scheme (GNU Guile)
swipl -g main -t halt graph.pl        # Prolog (SWI); SICStus: sicstus -l graph.pl --goal "main."
fpc graph.pas && ./graph              # Pascal (Free Pascal)
```

## Tools (Python + C++)

Utilities that **generate** or **check** graph work rather than solve it — so
they help with the labs and Project 3 without being submittable answers. 

| Tool | Files | What it does |
|------|-------|--------------|
| Test-data generator & converter | [`graph_generator.py`](graph_generator.py), [`graph_generator.cpp`](graph_generator.cpp) | Generates random directed/undirected/weighted graphs (and DAGs) at a tunable density; exports edge list, adjacency matrix, and Graphviz DOT. Gives you inputs to exercise your own code. |
| Solution verifiers | [`verify_solutions.py`](verify_solutions.py), [`verify_solutions.cpp`](verify_solutions.cpp) | Checks a claimed answer is correct **without computing it**: topological order (every edge points forward), shortest paths (no edge can still relax + tight predecessor tree), and minimum spanning tree (spanning + acyclic + minimal via the cycle property). |

Neither tool implements a traversal, MST, or shortest-path algorithm — the
generator only builds inputs, and the verifiers only validate output (each ships
with a built-in PASS/FAIL demo). Paste the generator's DOT output into an online
Graphviz viewer to draw the graph.

```bash
python3 graph_generator.py
g++ -std=c++17 -O2 graph_generator.cpp -o graph_generator && ./graph_generator

python3 verify_solutions.py
g++ -std=c++17 -O2 verify_solutions.cpp -o verify_solutions && ./verify_solutions
```
