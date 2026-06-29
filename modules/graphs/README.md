# Graphs

Introduction to graphs, graph terminology, directed vs.  undirected vs. weighted graphs,
 and the two standard representations (adjacency list and adjacency matrix).

## Videos

- [Introduction to Graphs](https://youtu.be/9zsHWI9vv8g) (8:21): graph terminology and types of graphs (undirected, directed, & weighted).
- [Graph Algorithms](https://youtu.be/UJd3A0nrXg8) (7:59): breadth- and depth-first traversals, spanning trees, and representing graphs with adjacency matrices & adjacency lists.

## Graph data structure

A simple adjacency-list graph that supports directed and undirected weighted
edges, with `add vertex` and `add edge` operations, neighbor lookup, and edge
weight lookup.

> Building a graph representation is a car part of  **Project 3**  
> **(AI-Assisted Graph Algorithms)**, where you will implement a graph
> in the language of your choice. These examples are therefore provided
> only in non-mainstream languages (Go, Scheme, Prolog, Pascal) and on a
> **different graph** than any assignment.

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
