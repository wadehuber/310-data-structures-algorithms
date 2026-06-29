"""
Sweep-Line Segment Intersection Detection  (CSC310 Module 15)
============================================================

ANY-SEGMENTS-INTERSECT (CLRS 3e, Ch. 33): sweep a vertical line left to right,
processing segment endpoints in x-order.  Keep the segments currently crossing
the line in a status structure ordered by their y at the sweep line; two
segments can only intersect once they become adjacent in that order, so each
event only checks new neighbor pairs.  Result: O(n log n) instead of O(n^2).

A brute-force O(n^2) all-pairs checker is included to VERIFY the sweep result.
(For clarity the status structure is a Python list kept in sorted order; a
production version uses a balanced BST, as the notes describe.)
"""
from geometric_primitives import segments_intersect


def normalize(seg):
    """Return ((xL,yL),(xR,yR)) with the left endpoint first."""
    a, b = seg
    return (a, b) if a <= b else (b, a)


def y_at(seg, x):
    (x1, y1), (x2, y2) = seg
    if x2 == x1:
        return y1
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


def any_segments_intersect(segments):
    """Sweep-line detection. Returns a (i, j) pair that intersects, or None."""
    segs = [normalize(s) for s in segments]
    events = []  # (x, is_right, y, index)
    for i, s in enumerate(segs):
        events.append((s[0][0], 0, s[0][1], i))   # left endpoint
        events.append((s[1][0], 1, s[1][1], i))   # right endpoint
    events.sort()

    status = []  # indices of active segments, kept ordered by y at sweep line

    def hit(i, j):
        return segments_intersect(segs[i][0], segs[i][1], segs[j][0], segs[j][1])

    for x, is_right, _, i in events:
        if not is_right:                            # LEFT endpoint: insert
            pos = 0
            while pos < len(status) and y_at(segs[status[pos]], x) < y_at(segs[i], x):
                pos += 1
            status.insert(pos, i)
            if pos > 0 and hit(i, status[pos - 1]):
                return (i, status[pos - 1])
            if pos + 1 < len(status) and hit(i, status[pos + 1]):
                return (i, status[pos + 1])
        else:                                       # RIGHT endpoint: remove
            pos = status.index(i)
            if 0 < pos < len(status) - 1 and hit(status[pos - 1], status[pos + 1]):
                return (status[pos - 1], status[pos + 1])
            status.pop(pos)
    return None


def brute_force(segments):
    """O(n^2) verifier: any intersecting pair, or None."""
    for i in range(len(segments)):
        for j in range(i + 1, len(segments)):
            a, b = normalize(segments[i]), normalize(segments[j])
            if segments_intersect(a[0], a[1], b[0], b[1]):
                return (i, j)
    return None


def main():
    # Demo set (distinct from the Lab 15 segments).
    segments = [
        ((1, 1), (6, 5)),     # 0
        ((2, 6), (7, 1)),     # 1  crosses 0
        ((8, 1), (10, 4)),    # 2  off on its own
    ]
    print("Segments:")
    for i, s in enumerate(segments):
        print(f"  s{i}: {s[0]} -> {s[1]}")
    res = any_segments_intersect(segments)
    print(f"\nSweep-line result: {'intersection between s'+str(res[0])+' and s'+str(res[1]) if res else 'no intersection'}")

    print("\nVerification against brute force on 2000 random instances:")
    import random
    rng = random.Random(1)
    ok = True
    for _ in range(2000):
        segs = [((rng.randint(0, 9), rng.randint(0, 9)),
                 (rng.randint(0, 9), rng.randint(0, 9))) for _ in range(5)]
        segs = [s for s in segs if s[0] != s[1] and s[0][0] != s[1][0]]  # no points/verticals
        if (any_segments_intersect(segs) is None) != (brute_force(segs) is None):
            ok = False
            print("  MISMATCH:", segs)
            break
    print("  sweep-line agrees with brute force on every instance" if ok else "  found a mismatch")


if __name__ == "__main__":
    main()
