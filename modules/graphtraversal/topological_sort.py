"""
Topological Sort  (CSC310 Module 7 - Graph Algorithms)
======================================================

A topological sort of a directed acyclic graph (DAG) is a linear ordering of the
vertices such that for every edge (u, v), u appears before v.  The DFS method
from the notes: run DFS and output vertices in DECREASING order of finish time
(prepend each vertex as it finishes).  A back edge (a GRAY neighbor) means the
graph has a cycle and no topological order exists.

Time: O(|V| + |E|).
"""

WHITE, GRAY, BLACK = 0, 1, 2


def topological_sort(adj):
    color = {u: WHITE for u in adj}
    order = []           # vertices prepended in reverse finish order
    has_cycle = [False]

    def dfs_visit(u):
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == WHITE:
                dfs_visit(v)
            elif color[v] == GRAY:      # back edge -> cycle
                has_cycle[0] = True
        color[u] = BLACK
        order.insert(0, u)              # finished: prepend

    for u in adj:
        if color[u] == WHITE:
            dfs_visit(u)
    return (None if has_cycle[0] else order)


def main():
    # CLRS "getting dressed" DAG -- a classic dependency example (not used in any
    # CSC310 assignment).  Edge u -> v means "u must be put on before v".
    adj = {
        "undershorts": ["pants", "shoes"],
        "pants":       ["belt", "shoes"],
        "belt":        ["jacket"],
        "shirt":       ["belt", "tie"],
        "tie":         ["jacket"],
        "jacket":      [],
        "socks":       ["shoes"],
        "shoes":       [],
        "watch":       [],
    }
    order = topological_sort(adj)
    print("Dependency edges (u must come before v):")
    for u in adj:
        for v in adj[u]:
            print(f"  {u} -> {v}")
    print()
    if order is None:
        print("Graph has a cycle: no topological ordering exists.")
    else:
        print("A valid topological order:")
        print("  " + " -> ".join(order))


if __name__ == "__main__":
    main()
