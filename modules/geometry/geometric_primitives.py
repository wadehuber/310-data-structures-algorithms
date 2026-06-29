"""
Geometric Primitives: Orientation & Segment Intersection  (CSC310 Module 15)
===========================================================================

orientation(p, q, r): the cross product (q-p) x (r-p)
    > 0  -> counterclockwise (left) turn at q
    < 0  -> clockwise (right) turn at q
    = 0  -> collinear
"""


def orientation(p, q, r):
    """Cross product of (q - p) and (r - p)."""
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def turn(p, q, r):
    c = orientation(p, q, r)
    return "left (CCW)" if c > 0 else "right (CW)" if c < 0 else "collinear"


def on_segment(p, q, r):
    """Assuming p, q, r collinear, is q on segment pr?"""
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))


def segments_intersect(p1, p2, p3, p4):
    """Do segments p1p2 and p3p4 intersect (including endpoints/collinear)?"""
    d1 = orientation(p3, p4, p1)
    d2 = orientation(p3, p4, p2)
    d3 = orientation(p1, p2, p3)
    d4 = orientation(p1, p2, p4)
    if ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 and d2 and d3 and d4:
        return True                      # proper crossing
    # collinear/touching cases
    if d1 == 0 and on_segment(p3, p1, p4): return True
    if d2 == 0 and on_segment(p3, p2, p4): return True
    if d3 == 0 and on_segment(p1, p3, p2): return True
    if d4 == 0 and on_segment(p1, p4, p2): return True
    return False


def main():
    print("Orientation test (cross product of (q-p) and (r-p)):")
    for p, q, r in [((0, 0), (4, 0), (2, 3)),
                    ((0, 0), (4, 0), (2, -3)),
                    ((0, 0), (4, 0), (2, 0))]:
        print(f"  {p}, {q}, {r}: cross={orientation(p, q, r):>4}  -> {turn(p, q, r)}")

    print("\nSegment intersection test:")
    cases = [
        (((0, 0), (4, 4)), ((0, 4), (4, 0)), "cross at (2,2)"),
        (((0, 0), (1, 1)), ((2, 2), (3, 3)), "collinear, disjoint"),
        (((0, 0), (2, 2)), ((3, 0), (4, 1)), "apart"),
        (((0, 0), (4, 0)), ((2, 0), (2, 3)), "T-touch at (2,0)"),
    ]
    for s1, s2, label in cases:
        hit = segments_intersect(s1[0], s1[1], s2[0], s2[1])
        print(f"  {s1} vs {s2}: {'INTERSECT' if hit else 'no':<9} ({label})")


if __name__ == "__main__":
    main()
