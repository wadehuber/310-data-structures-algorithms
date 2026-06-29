// Geometric Primitives: Orientation & Segment Intersection  (CSC310 Module 15)
// ===========================================================================
//
// Build:  g++ -std=c++17 -O2 geometric_primitives.cpp -o geometric_primitives && ./geometric_primitives
#include <iostream>
#include <string>

struct P { long x, y; };

// cross product of (q-p) and (r-p)
long orientation(P p, P q, P r) {
    return (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x);
}

std::string turn(P p, P q, P r) {
    long c = orientation(p, q, r);
    return c > 0 ? "left (CCW)" : c < 0 ? "right (CW)" : "collinear";
}

bool onSegment(P p, P q, P r) { // p,q,r collinear: is q on pr?
    return std::min(p.x, r.x) <= q.x && q.x <= std::max(p.x, r.x) &&
           std::min(p.y, r.y) <= q.y && q.y <= std::max(p.y, r.y);
}

bool segmentsIntersect(P p1, P p2, P p3, P p4) {
    long d1 = orientation(p3, p4, p1), d2 = orientation(p3, p4, p2);
    long d3 = orientation(p1, p2, p3), d4 = orientation(p1, p2, p4);
    if (((d1 > 0) != (d2 > 0)) && ((d3 > 0) != (d4 > 0)) && d1 && d2 && d3 && d4)
        return true;                       // proper crossing
    if (d1 == 0 && onSegment(p3, p1, p4)) return true;
    if (d2 == 0 && onSegment(p3, p2, p4)) return true;
    if (d3 == 0 && onSegment(p1, p3, p2)) return true;
    if (d4 == 0 && onSegment(p1, p4, p2)) return true;
    return false;
}

int main() {
    std::cout << "Orientation test (cross product of (q-p) and (r-p)):\n";
    P trips[][3] = {{{0,0},{4,0},{2,3}}, {{0,0},{4,0},{2,-3}}, {{0,0},{4,0},{2,0}}};
    for (auto& t : trips)
        std::cout << "  (" << t[0].x << "," << t[0].y << "), (" << t[1].x << ","
                  << t[1].y << "), (" << t[2].x << "," << t[2].y << "): cross="
                  << orientation(t[0], t[1], t[2]) << " -> " << turn(t[0], t[1], t[2]) << "\n";

    std::cout << "\nSegment intersection test:\n";
    struct C { P a, b, c, d; const char* label; } cases[] = {
        {{0,0},{4,4},{0,4},{4,0}, "cross at (2,2)"},
        {{0,0},{1,1},{2,2},{3,3}, "collinear, disjoint"},
        {{0,0},{2,2},{3,0},{4,1}, "apart"},
        {{0,0},{4,0},{2,0},{2,3}, "T-touch at (2,0)"},
    };
    for (auto& c : cases)
        std::cout << "  " << (segmentsIntersect(c.a, c.b, c.c, c.d) ? "INTERSECT" : "no")
                  << "  (" << c.label << ")\n";
    return 0;
}
