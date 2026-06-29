# CSC310 Module Code Examples

Runnable code examples for **CSC310 — Data Structures and Algorithms**, organized
by course module. Each folder complements that module's notes with working code,
and most topics are implemented in several languages so you can read whichever is
most familiar.

> **These examples are learning companions to the notes — not solutions to the
> labs, homework, or projects.** Where a topic is something you implement in an
> assignment (for example a traversal, an MST or shortest-path algorithm, a
> graph data structure, union-find, a balanced tree, or a convex hull), the
> example here is deliberately given in a non-mainstream language and/or on a
> different input, so it illustrates the idea without being a drop-in answer.
> Each folder's README notes any such overlap.

Languages used across the repo: **Python, Java, C++, C, Go, Scheme, Prolog,
Pascal.** Chapter/section references follow **CLRS** — *Introduction to
Algorithms*, 4th edition (Cormen, Leiserson, Rivest, Stein).

## Unit 1 — Algorithm Analysis & Sorting

| Module | Topic | CLRS | Folder | Languages |
|--------|-------|------|--------|-----------|
| 0 | Data Structures Review (lists, stacks, queues, trees) | Ch. 10 | [`elementarydatastructures`](elementarydatastructures/) | Java |
| 1 | Algorithm Analysis (growth, asymptotics, recurrences) | Ch. 2–3, App. A | [`algorithmanalysis`](algorithmanalysis/) | Java, Python, Scheme, Prolog |
| 2 | Heaps & Priority Queues | Ch. 6 | [`heaps`](heaps/) | Java, Python, C++, Prolog |
| 2 | Quicksort (partitioning, pivot strategies) | Ch. 7 | [`quicksort`](quicksort/) | Java, C++, Python, Go, Scheme, Prolog |
| 3A | Sorting in Linear Time (counting, radix, bucket) | Ch. 8 | [`sorting`](sorting/) | Python, Java, C++, Scheme |
| 3B | Medians & Order Statistics (quickselect, median-of-medians) | Ch. 9 | [`statistics`](statistics/) | Python, Java, C++, Scheme |

## Unit 2 — Fundamental Data Structures

| Module | Topic | CLRS | Folder | Languages |
|--------|-------|------|--------|-----------|
| 4A | Data Structures Review | Ch. 10 | [`elementarydatastructures`](elementarydatastructures/) | Java |
| 4B | Hashing & Hash Tables | Ch. 11 | [`hashtables`](hashtables/) | Python, C++, Scheme, Java |
| 5 | Binary, Search & Balanced Trees | Ch. 12, 13, 18 | [`trees`](trees/) | Python, C++, Scheme, Java |
| 6A | Disjoint Sets (union-find) | Ch. 19 | [`disjointsets`](disjointsets/) | Python, Go, Scheme, Prolog |
| 6B | Graphs (representations) | Ch. 20.1 | [`graphs`](graphs/) | Go, Scheme, Prolog, Pascal |

## Unit 3 — Graph Algorithms

| Module | Topic | CLRS | Folder | Languages |
|--------|-------|------|--------|-----------|
| 7 | Graph Search & Traversal (BFS, DFS, topo sort, SCC) | Ch. 20.2–20.5 | [`graphtraversal`](graphtraversal/) | Python, Java, C++, Prolog |
| 8 | *Midterm — no code* | — | — | — |
| 9 | Spanning Trees (Kruskal, Prim) | Ch. 21 | [`spanningtrees`](spanningtrees/) | Scheme, Go, Python |
| 10 | Shortest Paths (Dijkstra, Bellman-Ford, Floyd-Warshall) | Ch. 22–23 | [`shortestpaths`](shortestpaths/) | Go, Prolog, Scheme |

## Unit 4 — Advanced Algorithm Design

| Module | Topic | CLRS | Folder | Languages |
|--------|-------|------|--------|-----------|
| 11 | Dynamic Programming (rod cutting, matrix chain, optimal BST) | Ch. 14 | [`dynamicprogramming`](dynamicprogramming/) | Python, Java, Scheme, Go |
| 12 | Greedy Algorithms (activity selection, Huffman, caching) | Ch. 15 | [`greedyalgorithms`](greedyalgorithms/) | Python, C++, Java, Prolog |
| 13 | Randomized Algorithms (Miller-Rabin, Monte Carlo, balls & bins) | Ch. 5 | [`randomizedalgorithms`](randomizedalgorithms/) | Python, C++, C, Scheme |

## Unit 5 — Applications

| Module | Topic | CLRS | Folder | Languages |
|--------|-------|------|--------|-----------|
| 14 | String Algorithms (KMP, Rabin-Karp, suffix arrays) | Ch. 32 | [`stringalgorithms`](stringalgorithms/) | Python, Java, C++, C |
| 15 | Computational Geometry (orientation, sweep line, convex hull) | Ch. 33.1–33.3 † | [`geometry`](geometry/) | Python, C++, Scheme, Go |
| 16 | *Final — no code* | — | — | — |

† Chapter 33 (Computational Geometry) is in CLRS **3rd edition**; it was removed
from the 4th edition but remains available as a free download.

## Running the examples

Each folder's README lists exact build/run commands. In general:

```bash
python3 file.py                                   # Python
javac File.java && java File                      # Java
g++ -std=c++17 -O2 file.cpp -o file && ./file     # C++
gcc -O2 file.c -o file && ./file                  # C
go run file.go                                    # Go
guile file.scm                                    # Scheme (GNU Guile)
swipl -g main -t halt file.pl                     # Prolog (SWI)
fpc file.pas && ./file                            # Pascal (Free Pascal)
```

NOTE: *Modules 8 and 16 are exam weeks with no code*.
