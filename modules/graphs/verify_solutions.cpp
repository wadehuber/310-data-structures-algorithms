// Graph Solution Verifiers  (CSC310 - Graphs)
// ===========================================
//
// UTILITY (safe).  These functions CHECK whether a claimed answer is correct;
// they do NOT compute it.  A verifier cannot be submitted as a Project 3 or lab
// solution -- it validates output produced some other way.  Port of
// verify_solutions.py.
//
//   verify_topological_order : every directed edge points forward in the order
//   verify_shortest_paths    : no edge can still relax (distances are feasible)
//   verify_mst               : claimed edges form a spanning tree AND are minimum
//                              (checked via the cycle property)
//
// Build:  g++ -std=c++17 -O2 verify_solutions.cpp -o verify_solutions && ./verify_solutions
#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using std::pair;
using std::string;
using std::vector;
using Edge = std::tuple<int, int, int>;

pair<bool, string> verifyTopo(int n, const vector<pair<int, int>>& edges,
                              const vector<int>& order) {
    vector<int> sorted_order = order;
    std::sort(sorted_order.begin(), sorted_order.end());
    for (int i = 0; i < n; ++i)
        if (sorted_order[i] != i) return {false, "order is not a permutation of all vertices"};
    vector<int> pos(n);
    for (int i = 0; i < (int)order.size(); ++i) pos[order[i]] = i;
    for (auto& [u, v] : edges)
        if (pos[u] >= pos[v])
            return {false, "edge " + std::to_string(u) + "->" + std::to_string(v) + " points backward"};
    return {true, "valid topological order"};
}

pair<bool, string> verifyShortestPaths(const vector<Edge>& edges, int source,
                                       const std::map<int, int>& dist) {
    auto it = dist.find(source);
    if (it == dist.end() || it->second != 0)
        return {false, "dist[source] should be 0"};
    for (auto& [u, v, w] : edges) {
        if (dist.at(u) + w < dist.at(v))
            return {false, "edge " + std::to_string(u) + "->" + std::to_string(v) +
                           " (w=" + std::to_string(w) + ") can still relax"};
    }
    return {true, "distances are correct shortest-path values"};
}

// heaviest edge weight on the unique tree path a..b (or -1 if unreachable)
int treePathMax(const std::map<int, vector<pair<int, int>>>& adj, int a, int b) {
    std::map<int, pair<int, int>> parent; // node -> (prev, weight)
    std::set<int> visited{a};
    parent[a] = {-1, -1};
    vector<int> stack{a};
    while (!stack.empty()) {
        int node = stack.back();
        stack.pop_back();
        if (node == b) break;
        auto it = adj.find(node);
        if (it == adj.end()) continue;
        for (auto& [nb, w] : it->second)
            if (!visited.count(nb)) {
                visited.insert(nb);
                parent[nb] = {node, w};
                stack.push_back(nb);
            }
    }
    if (!parent.count(b)) return -1;
    int cur = b, best = -1;
    while (parent[cur].first != -1) {
        best = std::max(best, parent[cur].second);
        cur = parent[cur].first;
    }
    return best;
}

pair<bool, string> verifyMST(int n, const vector<Edge>& all_edges,
                             const vector<Edge>& mst) {
    if ((int)mst.size() != n - 1)
        return {false, "spanning tree needs " + std::to_string(n - 1) + " edges"};
    vector<int> parent(n);
    for (int i = 0; i < n; ++i) parent[i] = i;
    std::function<int(int)> find = [&](int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    };
    for (auto& [u, v, w] : mst) {
        int ru = find(u), rv = find(v);
        if (ru == rv) return {false, "claimed tree contains a cycle"};
        parent[ru] = rv;
    }
    std::set<int> roots;
    for (int i = 0; i < n; ++i) roots.insert(find(i));
    if (roots.size() != 1) return {false, "claimed tree does not connect all vertices"};

    int total = 0;
    std::map<int, vector<pair<int, int>>> tadj;
    std::set<pair<int, int>> tset;
    for (auto& [u, v, w] : mst) {
        total += w;
        tadj[u].push_back({v, w});
        tadj[v].push_back({u, w});
        tset.insert({std::min(u, v), std::max(u, v)});
    }
    for (auto& [u, v, w] : all_edges) {
        if (tset.count({std::min(u, v), std::max(u, v)})) continue;
        int heaviest = treePathMax(tadj, u, v);
        if (heaviest != -1 && w < heaviest)
            return {false, "not minimal: non-tree edge " + std::to_string(u) + "-" +
                           std::to_string(v) + " (w=" + std::to_string(w) +
                           ") is lighter than tree-path max " + std::to_string(heaviest)};
    }
    return {true, "valid minimum spanning tree, total weight " + std::to_string(total)};
}

void report(const string& title, const pair<bool, string>& r) {
    std::cout << title << ": " << (r.first ? "PASS" : "FAIL") << " - " << r.second << "\n";
}

int main() {
    std::cout << "== Topological order ==\n";
    vector<pair<int, int>> dag = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {3, 4}};
    report("correct order [0,1,2,3,4]", verifyTopo(5, dag, {0, 1, 2, 3, 4}));
    report("bad order     [1,0,2,3,4]", verifyTopo(5, dag, {1, 0, 2, 3, 4}));

    std::cout << "\n== Shortest paths (source 0) ==\n";
    vector<Edge> sp = {{0,1,1},{0,2,4},{1,2,2},{1,3,6},{2,3,3},{3,4,1}};
    report("correct distances", verifyShortestPaths(sp, 0, {{0,0},{1,1},{2,3},{3,6},{4,7}}));
    report("bad distances    ", verifyShortestPaths(sp, 0, {{0,0},{1,1},{2,4},{3,6},{4,7}}));

    std::cout << "\n== Minimum spanning tree ==\n";
    vector<Edge> g = {{0,1,2},{0,2,3},{1,2,1},{1,3,4},{2,3,5},{3,4,6}};
    report("correct MST (w=13)", verifyMST(5, g, {{1,2,1},{0,1,2},{1,3,4},{3,4,6}}));
    report("non-minimal tree  ", verifyMST(5, g, {{1,2,1},{0,2,3},{1,3,4},{3,4,6}}));
    return 0;
}
