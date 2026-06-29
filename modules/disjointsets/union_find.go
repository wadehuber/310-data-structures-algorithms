// Disjoint-Set Forest (Union-Find)  (CSC310 Module 6A - Disjoint Sets)
// ===================================================================
//
// Forest-of-rooted-trees representation with the two optimizations from the
// notes: union by rank (keep trees shallow) and path compression (flatten on
// FIND-SET).  Amortized O(alpha(n)) per operation -- effectively constant.
//
// Run:  go run union_find.go
package main

import (
	"fmt"
	"sort"
)

type DSU struct {
	parent []int
	rank   []int
}

func NewDSU(n int) *DSU {
	d := &DSU{parent: make([]int, n), rank: make([]int, n)}
	for i := range d.parent { // MAKE-SET for each element
		d.parent[i] = i
	}
	return d
}

// Find returns the representative of x, compressing the path on the way up.
func (d *DSU) Find(x int) int {
	root := x
	for d.parent[root] != root {
		root = d.parent[root]
	}
	for d.parent[x] != root { // path compression
		d.parent[x], x = root, d.parent[x]
	}
	return root
}

// Union merges the sets containing x and y, linking by rank.
func (d *DSU) Union(x, y int) {
	rx, ry := d.Find(x), d.Find(y)
	if rx == ry {
		return
	}
	if d.rank[rx] > d.rank[ry] {
		rx, ry = ry, rx
	}
	d.parent[rx] = ry
	if d.rank[rx] == d.rank[ry] {
		d.rank[ry]++
	}
}

func (d *DSU) Connected(x, y int) bool { return d.Find(x) == d.Find(y) }

func (d *DSU) printSets() {
	groups := map[int][]int{}
	for x := range d.parent {
		r := d.Find(x)
		groups[r] = append(groups[r], x)
	}
	var sets [][]int
	for _, members := range groups {
		sort.Ints(members)
		sets = append(sets, members)
	}
	sort.Slice(sets, func(i, j int) bool { return sets[i][0] < sets[j][0] })
	fmt.Print("Sets: ")
	for _, s := range sets {
		fmt.Print("{")
		for i, m := range s {
			fmt.Print(m)
			if i+1 < len(s) {
				fmt.Print(", ")
			}
		}
		fmt.Print("} ")
	}
	fmt.Println()
}

func main() {
	d := NewDSU(7) // elements 0..6
	fmt.Println("Disjoint-set forest (union by rank + path compression)")
	fmt.Println("Operations: union(0,1) union(2,3) union(1,3) union(4,5)")
	d.Union(0, 1)
	d.Union(2, 3)
	d.Union(1, 3)
	d.Union(4, 5)
	d.printSets()
	fmt.Printf("connected(0,3)? %v\n", d.Connected(0, 3))
	fmt.Printf("connected(0,4)? %v\n", d.Connected(0, 4))
}
