# Computational Geometry

Code examples for **Module 15 — Computational Geometry** (CLRS 3e, Ch. 33).
Every algorithm here is built on the **cross product**,
which answers orientation questions without division or trigonometry and stays
exact on integer input.

## Examples

| Topic | Language(s) | Notes |
|-------|-------------|-------|
| Orientation & segment-intersection primitives | Python, C++ | Cross-product orientation test (left/right/collinear) and a segment-intersection test. |
| Sweep-line segment intersection | Python | `ANY-SEGMENTS-INTERSECT`: O(n log n) detection, verified against an O(n²) brute-force checker on 2000 random instances. |
| Convex hull — Graham's scan | Scheme | Esoteric language, different points; prints hull only (no `points.txt`, no image). |
| Convex hull — Jarvis's march | Go | Esoteric language, different points; prints hull only. |

Graham's scan and Jarvis's march compute the **same** hull
(`(0,0) (2,0) (4,1) (4,4) (2,5) (0,3)`) on the demo point set, by different
routes.

## What each shows

- **Primitives** — the orientation test is a single cross product; segment
  intersection is four orientation tests plus collinear/touching checks. These
  power everything else.
- **Sweep line** — instead of comparing all O(n²) segment pairs, sweep a vertical
  line left to right and keep active segments ordered by height; two segments can
  only intersect once they become neighbors, so each event checks just a couple
  of pairs. (The status structure here is a sorted list standing in for the
  balanced BST the notes describe.)
- **Graham's scan** — sort points by polar angle around the lowest point (via the
  cross product), then sweep with a stack, popping any non-left turn. O(n log n).
- **Jarvis's march** — "gift wrapping": from the lowest point, repeatedly pick
  the most clockwise next point until you wrap around. O(n·h).

## Running

```bash
python3 geometric_primitives.py
g++ -std=c++17 -O2 geometric_primitives.cpp -o geometric_primitives && ./geometric_primitives

python3 sweep_line_intersection.py

guile graham_scan.scm        # Scheme (GNU Guile)
go run jarvis_march.go       # Go
```

## Where each ties back to the notes

- *Geometric Primitives / Orientation Test* → `geometric_primitives.py`, `geometric_primitives.cpp`
- *Sweep Line Algorithms (ANY-SEGMENTS-INTERSECT)* → `sweep_line_intersection.py`
- *Convex Hull — Graham's Scan* → `graham_scan.scm`
- *Convex Hull — Jarvis's March* → `jarvis_march.go`
