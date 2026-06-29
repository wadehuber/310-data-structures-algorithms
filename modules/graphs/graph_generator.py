"""
Graph Test-Data Generator & Format Converter  (CSC310 - Graphs)
==============================================================

UTILITY (safe).  This is a tool, not an algorithm: it builds random graphs you
can feed to your own code (e.g. Project 3) and converts a graph among three
formats.  It does NOT implement any traversal, MST, or shortest-path algorithm.

Generates directed/undirected, optionally weighted graphs with a tunable edge
density, plus a DAG mode (only forward edges u<v, so it is acyclic).  Exports to:
  - edge list
  - adjacency matrix
  - Graphviz DOT (paste into https://dreampuf.github.io/GraphvizOnline to draw)
"""
import random


def generate(n, density=0.4, directed=False, weighted=True,
             weight_range=(1, 9), dag=False, seed=None):
    """Return (n, edges) where edges is a list of (u, v, w) (w=1 if unweighted)."""
    rng = random.Random(seed)
    edges = []
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if not directed and v < u:
                continue                      # undirected: emit each pair once
            if dag and v <= u:
                continue                      # DAG: only forward edges
            if rng.random() < density:
                w = rng.randint(*weight_range) if weighted else 1
                edges.append((u, v, w))
    return n, edges


def to_edge_list(n, edges):
    lines = [f"# {n} vertices, {len(edges)} edges (u v w)"]
    lines += [f"{u} {v} {w}" for u, v, w in edges]
    return "\n".join(lines)


def to_adjacency_matrix(n, edges, directed=False):
    INF = 0  # 0 means "no edge" here; change to a sentinel if 0 is a valid weight
    m = [[INF] * n for _ in range(n)]
    for u, v, w in edges:
        m[u][v] = w
        if not directed:
            m[v][u] = w
    header = "    " + " ".join(f"{j:>3}" for j in range(n))
    rows = [header]
    for i in range(n):
        rows.append(f"{i:>3} " + " ".join(f"{m[i][j]:>3}" for j in range(n)))
    return "\n".join(rows)


def to_dot(n, edges, directed=False):
    kind = "digraph" if directed else "graph"
    connector = "->" if directed else "--"
    lines = [f"{kind} G {{"]
    for v in range(n):
        lines.append(f"  {v};")
    for u, v, w in edges:
        lines.append(f'  {u} {connector} {v} [label="{w}"];')
    lines.append("}")
    return "\n".join(lines)


def main():
    # Reproducible demo: a small undirected weighted graph.
    n, edges = generate(n=6, density=0.45, directed=False, weighted=True, seed=7)
    print("=== Edge list ===")
    print(to_edge_list(n, edges))
    print("\n=== Adjacency matrix (0 = no edge) ===")
    print(to_adjacency_matrix(n, edges, directed=False))
    print("\n=== Graphviz DOT ===")
    print(to_dot(n, edges, directed=False))


if __name__ == "__main__":
    main()
