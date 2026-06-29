"""
DFS Edge Classification  (CSC310 Module 7 - Graph Algorithms)
============================================================

During a DFS of a directed graph, every edge (u, v) is one of four types:
  Tree    : v is discovered for the first time via (u, v)        (v is WHITE)
  Back    : v is an ancestor of u (still on the DFS stack)        (v is GRAY)
  Forward : v is a proper descendant, reached by a non-tree edge  (u.d < v.d)
  Cross   : everything else (different subtree / earlier finished) (u.d > v.d)
Back edges are exactly the edges that reveal a cycle.

Time: O(|V| + |E|).
"""

WHITE, GRAY, BLACK = 0, 1, 2


def classify_edges(adj):
    color = {u: WHITE for u in adj}
    disc = {u: 0 for u in adj}
    fin = {u: 0 for u in adj}
    time = [0]
    edges = {"tree": [], "back": [], "forward": [], "cross": []}

    def dfs_visit(u):
        time[0] += 1
        disc[u] = time[0]
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == WHITE:
                edges["tree"].append((u, v))
                dfs_visit(v)
            elif color[v] == GRAY:
                edges["back"].append((u, v))
            elif disc[u] < disc[v]:        # v already BLACK, discovered later
                edges["forward"].append((u, v))
            else:
                edges["cross"].append((u, v))
        color[u] = BLACK
        time[0] += 1
        fin[u] = time[0]

    for u in adj:
        if color[u] == WHITE:
            dfs_visit(u)
    return edges, disc, fin


def main():
    # CLRS Fig. 22.4 directed graph (classic edge-classification example).
    adj = {
        "u": ["v", "x"],
        "v": ["y"],
        "w": ["y", "z"],
        "x": ["v"],
        "y": ["x"],
        "z": ["z"],
    }
    edges, disc, fin = classify_edges(adj)

    print("Discovery/finish times (d/f):")
    for u in adj:
        print(f"  {u}: {disc[u]}/{fin[u]}")
    print()
    for kind in ("tree", "back", "forward", "cross"):
        pairs = ", ".join(f"{u}->{v}" for u, v in edges[kind])
        print(f"  {kind.capitalize():8}: {pairs if pairs else '(none)'}")
    print()
    print(f"Cycle present? {'yes' if edges['back'] else 'no'} "
          f"(a back edge exists iff the graph has a cycle).")


if __name__ == "__main__":
    main()
