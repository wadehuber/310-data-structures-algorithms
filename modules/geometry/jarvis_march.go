// Jarvis's March (Gift Wrapping) - Convex Hull  (CSC310 Module 15)
// ================================================================
//
// Jarvis's march ("gift wrapping"): start at the lowest point and repeatedly
// pick the most counterclockwise next point relative to the current hull edge,
// until you wrap back to the start.  O(n*h) for h hull vertices.
//
// Run:  go run jarvis_march.go
package main

import "fmt"

type Point struct{ x, y int }

// cross product of (a-o) and (b-o): >0 left turn, <0 right turn, 0 collinear
func cross(o, a, b Point) int {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func dist2(a, b Point) int {
	dx, dy := a.x-b.x, a.y-b.y
	return dx*dx + dy*dy
}

func jarvisMarch(pts []Point) []Point {
	n := len(pts)
	if n < 3 {
		return pts
	}
	// start at the lowest point (min y, then min x)
	start := 0
	for i, p := range pts {
		if p.y < pts[start].y || (p.y == pts[start].y && p.x < pts[start].x) {
			start = i
		}
	}

	var hull []Point
	cur := start
	for {
		hull = append(hull, pts[cur])
		next := (cur + 1) % n
		for i := 0; i < n; i++ {
			c := cross(pts[cur], pts[next], pts[i])
			// pick the most clockwise-from-next point (keeps everyone to the left),
			// breaking ties by taking the farthest collinear point
			if c < 0 || (c == 0 && dist2(pts[cur], pts[i]) > dist2(pts[cur], pts[next])) {
				next = i
			}
		}
		cur = next
		if cur == start {
			break
		}
	}
	return hull
}

func main() {
	pts := []Point{
		{0, 0}, {2, 0}, {4, 1}, {4, 4}, {2, 5},
		{0, 3}, {2, 2}, {1, 1}, {3, 2},
	}
	hull := jarvisMarch(pts)
	fmt.Println("Convex hull (Jarvis's march), CCW from the lowest point:")
	for _, p := range hull {
		fmt.Printf("  %d %d\n", p.x, p.y)
	}
	fmt.Printf("(%d hull vertices)\n", len(hull))
}
