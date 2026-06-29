// Prim's Minimum Spanning Tree  (CSC310 Module 9 - Spanning Trees)
// ================================================================
//
// Prim: grow one tree from a start vertex, repeatedly adding the cheapest edge
// that connects the tree to a vertex outside it.  Expected total weight: 14.
//
// Run:  go run prim.go
package main

import (
	"fmt"
	"sort"
)

type Edge struct{ u, v, w int }

const numVertices = 6

// Undirected weighted edges.  DISTINCT from every assignment graph.
var edges = []Edge{
	{0, 1, 4}, {0, 2, 3}, {1, 2, 1}, {1, 3, 2},
	{2, 3, 4}, {3, 4, 2}, {4, 5, 6}, {3, 5, 8}, {2, 4, 5},
}

func prim(start int) ([]Edge, int) {
	adj := make(map[int][]Edge)
	for _, e := range edges { // build undirected adjacency
		adj[e.u] = append(adj[e.u], Edge{e.u, e.v, e.w})
		adj[e.v] = append(adj[e.v], Edge{e.v, e.u, e.w})
	}
	inTree := make([]bool, numVertices)
	inTree[start] = true
	var mst []Edge
	total := 0

	for len(mst) < numVertices-1 {
		// cheapest edge from the tree to a vertex outside it
		best := Edge{-1, -1, 1 << 30}
		for v := 0; v < numVertices; v++ {
			if !inTree[v] {
				continue
			}
			for _, e := range adj[v] {
				if !inTree[e.v] && e.w < best.w {
					best = e
				}
			}
		}
		if best.u == -1 {
			break // disconnected
		}
		inTree[best.v] = true
		mst = append(mst, best)
		total += best.w
	}
	sort.Slice(mst, func(i, j int) bool { return mst[i].w < mst[j].w })
	return mst, total
}

func main() {
	mst, total := prim(0)
	fmt.Println("Prim's MST edges (u v w):")
	for _, e := range mst {
		fmt.Printf("  (%d %d %d)\n", e.u, e.v, e.w)
	}
	fmt.Printf("Total weight: %d\n", total)
}
