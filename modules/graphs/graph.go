// Simple Graph Data Structure  (CSC310 Module 6B - Graphs)
// ========================================================
//
// Adjacency-list representation using a map from vertex name to a slice of
// (neighbor, weight) edges, plus an ordered list of vertices for stable output.
//
// Run:  go run graph.go
package main

import (
	"fmt"
	"sort"
)

type Edge struct {
	to     string
	weight int
}

type Graph struct {
	order []string           // insertion order, for stable printing
	adj   map[string][]Edge  // vertex -> outgoing edges
}

func NewGraph() *Graph {
	return &Graph{adj: make(map[string][]Edge)}
}

func (g *Graph) AddVertex(v string) {
	if _, ok := g.adj[v]; !ok {
		g.adj[v] = []Edge{}
		g.order = append(g.order, v)
	}
}

// AddEdge adds u->v with the given weight; if !directed it also adds v->u.
func (g *Graph) AddEdge(u, v string, w int, directed bool) {
	g.AddVertex(u)
	g.AddVertex(v)
	g.adj[u] = append(g.adj[u], Edge{v, w})
	if !directed {
		g.adj[v] = append(g.adj[v], Edge{u, w})
	}
}

func (g *Graph) Neighbors(v string) []Edge {
	es := append([]Edge(nil), g.adj[v]...)
	sort.Slice(es, func(i, j int) bool { return es[i].to < es[j].to })
	return es
}

func (g *Graph) Print() {
	fmt.Println("Graph (undirected, weighted) - adjacency list:")
	for _, v := range g.order {
		fmt.Printf("  %s -> ", v)
		es := g.Neighbors(v)
		for i, e := range es {
			fmt.Printf("%s(%d)", e.to, e.weight)
			if i+1 < len(es) {
				fmt.Print(", ")
			}
		}
		fmt.Println()
	}
}

func main() {
	g := NewGraph()
	// A small Arizona road network (miles).  Not an assignment graph.
	for _, v := range []string{"PHX", "TUS", "MESA", "TEMPE"} {
		g.AddVertex(v)
	}
	g.AddEdge("PHX", "MESA", 20, false)
	g.AddEdge("PHX", "TEMPE", 11, false)
	g.AddEdge("MESA", "TEMPE", 8, false)
	g.AddEdge("PHX", "TUS", 116, false)
	g.AddEdge("TUS", "MESA", 100, false)

	g.Print()

	fmt.Print("Neighbors of PHX: ")
	ns := g.Neighbors("PHX")
	for i, e := range ns {
		fmt.Print(e.to)
		if i+1 < len(ns) {
			fmt.Print(", ")
		}
	}
	fmt.Println()
	for _, e := range g.adj["PHX"] {
		if e.to == "MESA" {
			fmt.Printf("Weight PHX-MESA: %d\n", e.weight)
		}
	}
}
