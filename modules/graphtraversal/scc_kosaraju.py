"""
Strongly Connected Components - Kosaraju's Algorithm  (CSC310 Module 7)
=====================================================================

A strongly connected component of a directed graph is a maximal set of vertices
where every vertex can reach every other.  Kosaraju's algorithm:
  1. DFS on G, pushing each vertex onto a stack as it FINISHES.
  2. Build the transpose G^T (reverse every edge).
  3. DFS on G^T, popping start vertices off the stack; each DFS tree is one SCC.

Time: O(|V| + |E|).
"""


def kosaraju(adj):
    # 1. order vertices by finish time (first DFS on G)
    visited = set()
    finish_stack = []

    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        finish_stack.append(u)

    for u in adj:
        if u not in visited:
            dfs1(u)

    # 2. transpose
    transpose = {u: [] for u in adj}
    for u in adj:
        for v in adj[u]:
            transpose[v].append(u)

    # 3. DFS on transpose in decreasing finish order
    visited.clear()
    components = []

    def dfs2(u, comp):
        visited.add(u)
        comp.append(u)
        for v in transpose[u]:
            if v not in visited:
                dfs2(v, comp)

    for u in reversed(finish_stack):
        if u not in visited:
            comp = []
            dfs2(u, comp)
            components.append(sorted(comp))
    return components


def main():
    # CLRS Fig. 22.9 directed graph (a classic SCC example, not in any assignment)
    adj = {
        "a": ["b"],
        "b": ["c", "e", "f"],
        "c": ["d", "g"],
        "d": ["c", "h"],
        "e": ["a", "f"],
        "f": ["g"],
        "g": ["f", "h"],
        "h": ["h"],
    }
    print("Directed edges:")
    for u in adj:
        for v in adj[u]:
            print(f"  {u} -> {v}")
    print()
    comps = kosaraju(adj)
    print(f"Strongly connected components ({len(comps)}):")
    for c in comps:
        print("  {" + ", ".join(c) + "}")


if __name__ == "__main__":
    main()
