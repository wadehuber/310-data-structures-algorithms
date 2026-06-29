"""
Graph Solution Verifiers  (CSC310 - Graphs)
===========================================

These functions CHECK whether a claimed answer is correct; they do NOT compute
the answer.  Useful as a self-check: run your traversal / MST / shortest-path
output through these.

Includes:
  - verify_topological_order : every directed edge points forward in the order
  - verify_shortest_paths    : distances are feasible (no edge can relax) and,
                               if predecessors are given, each is achieved by a
                               tight tree edge from the source
  - verify_mst               : claimed edges form a spanning tree AND are minimum
                               (checked via the cycle property)
"""
from collections import defaultdict


# ---------- Topological order ----------
def verify_topological_order(n, directed_edges, order):
    if sorted(order) != list(range(n)):
        return False, "order is not a permutation of all vertices"
    pos = {v: i for i, v in enumerate(order)}
    for u, v in directed_edges:
        if pos[u] >= pos[v]:
            return False, f"edge {u}->{v} points backward (pos {pos[u]} >= {pos[v]})"
    return True, "valid topological order"


# ---------- Shortest paths ----------
def verify_shortest_paths(edges, source, dist, pred=None):
    if dist.get(source, None) != 0:
        return False, f"dist[source]={dist.get(source)} (should be 0)"
    # Feasibility: no edge may still be relaxed (triangle inequality is tight).
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return False, f"edge {u}->{v} (w={w}) can still relax: {dist[u]}+{w} < {dist[v]}"
    # Achievability: each non-source vertex's distance is realized by a tight
    # predecessor edge leading back toward the source.
    if pred is not None:
        adj = {(u, v): w for u, v, w in edges}
        for v in dist:
            if v == source:
                continue
            p = pred.get(v)
            if p is None:
                return False, f"vertex {v} has no predecessor"
            w = adj.get((p, v))
            if w is None or dist[p] + w != dist[v]:
                return False, f"dist[{v}]={dist[v]} not achieved by tight edge {p}->{v}"
    return True, "distances are correct shortest-path values"


# ---------- Minimum spanning tree ----------
def _tree_path_max(tree_adj, start, goal):
    """Heaviest edge weight on the unique path start..goal in a tree (or None)."""
    stack = [(start, None, -1)]
    visited = {start}
    parent = {start: (None, -1)}
    while stack:
        node, _, _ = stack.pop()
        if node == goal:
            break
        for nb, w in tree_adj[node]:
            if nb not in visited:
                visited.add(nb)
                parent[nb] = (node, w)
                stack.append((nb, node, w))
    if goal not in parent:
        return None
    cur, best = goal, -1
    while parent[cur][0] is not None:
        prev, w = parent[cur]
        best = max(best, w)
        cur = prev
    return best


def verify_mst(n, all_edges, mst_edges):
    if len(mst_edges) != n - 1:
        return False, f"a spanning tree of {n} vertices needs {n-1} edges, got {len(mst_edges)}"
    # spanning + acyclic via union-find
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v, w in mst_edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False, f"edge {u}-{v} creates a cycle (not a tree)"
        parent[ru] = rv
    roots = {find(x) for x in range(n)}
    if len(roots) != 1:
        return False, "claimed tree does not connect all vertices"

    total = sum(w for _, _, w in mst_edges)

    # minimality via the cycle property: every non-tree edge must be at least as
    # heavy as the heaviest edge on the tree path between its endpoints.
    tree_adj = defaultdict(list)
    tree_set = {frozenset((u, v)) for u, v, _ in mst_edges}
    for u, v, w in mst_edges:
        tree_adj[u].append((v, w))
        tree_adj[v].append((u, w))
    for u, v, w in all_edges:
        if frozenset((u, v)) in tree_set:
            continue
        heaviest = _tree_path_max(tree_adj, u, v)
        if heaviest is not None and w < heaviest:
            return False, (f"not minimal: non-tree edge {u}-{v} (w={w}) is lighter "
                           f"than tree-path max {heaviest}")
    return True, f"valid minimum spanning tree, total weight {total}"


def _report(title, result):
    ok, msg = result
    print(f"{title}: {'PASS' if ok else 'FAIL'} - {msg}")


def main():
    print("== Topological order ==")
    dag = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    _report("correct order [0,1,2,3,4]", verify_topological_order(5, dag, [0, 1, 2, 3, 4]))
    _report("bad order     [1,0,2,3,4]", verify_topological_order(5, dag, [1, 0, 2, 3, 4]))

    print("\n== Shortest paths (source 0) ==")
    sp = [(0, 1, 1), (0, 2, 4), (1, 2, 2), (1, 3, 6), (2, 3, 3), (3, 4, 1)]
    good = {0: 0, 1: 1, 2: 3, 3: 6, 4: 7}
    bad = {0: 0, 1: 1, 2: 4, 3: 6, 4: 7}   # dist[2] too big -> edge 1->2 relaxes
    _report("correct distances", verify_shortest_paths(sp, 0, good))
    _report("bad distances    ", verify_shortest_paths(sp, 0, bad))

    print("\n== Minimum spanning tree ==")
    g = [(0, 1, 2), (0, 2, 3), (1, 2, 1), (1, 3, 4), (2, 3, 5), (3, 4, 6)]
    good_mst = [(1, 2, 1), (0, 1, 2), (1, 3, 4), (3, 4, 6)]    # weight 13
    bad_mst = [(1, 2, 1), (0, 2, 3), (1, 3, 4), (3, 4, 6)]     # spanning but weight 14
    _report("correct MST (w=13)", verify_mst(5, g, good_mst))
    _report("non-minimal tree  ", verify_mst(5, g, bad_mst))


if __name__ == "__main__":
    main()
