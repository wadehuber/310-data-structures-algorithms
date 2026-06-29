// Dijkstra's Single-Source Shortest Paths  (CSC310 Module 10 - Shortest Paths)
// ===========================================================================
//
// Dijkstra (nonnegative weights): repeatedly "settle" the unsettled vertex with
// the smallest distance estimate, then relax its outgoing edges.  Once settled,
// a vertex's distance is final.  Expected: d(s,t,x,y,z) = 0,8,9,5,7.
//
// Run:  go run dijkstra.go
package main

import "fmt"

const INF = 1 << 30

type Edge struct {
	to string
	w  int
}

// Directed weighted graph, CLRS Fig. 24.6.  DISTINCT from every assignment graph.
var adj = map[string][]Edge{
	"s": {{"t", 10}, {"y", 5}},
	"t": {{"y", 2}, {"x", 1}},
	"y": {{"t", 3}, {"x", 9}, {"z", 2}},
	"x": {{"z", 4}},
	"z": {{"x", 6}, {"s", 7}},
}
var vertices = []string{"s", "t", "x", "y", "z"}

func dijkstra(source string) (map[string]int, map[string]string) {
	dist := map[string]int{}
	pred := map[string]string{}
	settled := map[string]bool{}
	for _, v := range vertices {
		dist[v] = INF
	}
	dist[source] = 0

	for range vertices {
		// pick the unsettled vertex with the smallest distance (EXTRACT-MIN)
		u, best := "", INF
		for _, v := range vertices {
			if !settled[v] && dist[v] < best {
				best, u = dist[v], v
			}
		}
		if u == "" {
			break
		}
		settled[u] = true
		for _, e := range adj[u] { // RELAX each outgoing edge
			if dist[u]+e.w < dist[e.to] {
				dist[e.to] = dist[u] + e.w
				pred[e.to] = u
			}
		}
	}
	return dist, pred
}

func main() {
	dist, pred := dijkstra("s")
	fmt.Println("Dijkstra from source s (CLRS Fig. 24.6):")
	fmt.Printf("  %-6s %-8s %s\n", "vertex", "dist", "pred")
	for _, v := range vertices {
		p := pred[v]
		if p == "" {
			p = "-"
		}
		fmt.Printf("  %-6s %-8d %s\n", v, dist[v], p)
	}
}
