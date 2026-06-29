"""
MST by Brute Force + the Cut & Cycle Properties  (CSC310 Module 9)
=================================================================

Exhaustive search is exponential, so it is only practical on tiny graphs; that is
exactly why the greedy algorithms exist.
"""
from itertools import combinations


# Undirected weighted graph (vertices 0..5).  DISTINCT from any assignment graph.
VERTICES = [0, 1, 2, 3, 4, 5]
EDGES = [
    (0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2),
    (2, 3, 4), (3, 4, 2), (4, 5, 6), (3, 5, 8), (2, 4, 5),
]


def connected(vertices, edges):
    """Is the vertex set connected using only the given edges?"""
    if not vertices:
        return True
    adj = {v: [] for v in vertices}
    for u, v, _ in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen, stack = {vertices[0]}, [vertices[0]]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == len(vertices)


def all_spanning_trees(vertices, edges):
    """Every (n-1)-edge subset that is connected is a spanning tree."""
    n = len(vertices)
    trees = []
    for combo in combinations(edges, n - 1):
        if connected(vertices, combo):
            trees.append(combo)
    return trees


def weight(tree):
    return sum(w for _, _, w in tree)


def main():
    trees = all_spanning_trees(VERTICES, EDGES)
    mst = min(trees, key=weight)
    print(f"Graph: {len(VERTICES)} vertices, {len(EDGES)} edges")
    print(f"Number of spanning trees (brute force): {len(trees)}")
    print(f"Minimum spanning tree weight: {weight(mst)}")
    print("MST edges:", sorted((u, v, w) for u, v, w in mst))
    mst_edges = {frozenset((u, v)) for u, v, _ in mst}
    print()

    # Cut property: for the cut ({0,1,2}, {3,4,5}), the lightest crossing edge
    # must be in the MST.
    S = {0, 1, 2}
    crossing = [(u, v, w) for u, v, w in EDGES if (u in S) ^ (v in S)]
    light = min(crossing, key=lambda e: e[2])
    print(f"Cut property: lightest edge crossing ({S}, rest) is {light}")
    print(f"  in MST? {frozenset((light[0], light[1])) in mst_edges}")
    print()

    # Cycle property: in the cycle 0-1-2-0, the heaviest edge must NOT be in MST.
    cycle = [(0, 1, 4), (1, 2, 1), (0, 2, 3)]
    heavy = max(cycle, key=lambda e: e[2])
    print(f"Cycle property: heaviest edge on cycle 0-1-2-0 is {heavy}")
    print(f"  in MST? {frozenset((heavy[0], heavy[1])) in mst_edges}")


if __name__ == "__main__":
    main()
