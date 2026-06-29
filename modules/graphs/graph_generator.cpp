// Graph Test-Data Generator & Format Converter  (CSC310 - Graphs)
// ===============================================================
//
// UTILITY (safe).  A tool, not an algorithm: it builds random graphs to feed to
// your own code (e.g. Project 3) and converts a graph among three formats.  It
// implements no traversal, MST, or shortest-path algorithm.
//
// Generates directed/undirected, optionally weighted graphs with a tunable
// density (and a DAG mode using only forward edges u<v).  Exports edge list,
// adjacency matrix, and Graphviz DOT.
//
// Build:  g++ -std=c++17 -O2 graph_generator.cpp -o graph_generator && ./graph_generator
#include <iomanip>
#include <iostream>
#include <random>
#include <tuple>
#include <vector>

using std::vector;
using Edge = std::tuple<int, int, int>; // (u, v, w)

vector<Edge> generate(int n, double density, bool directed, bool weighted,
                      int wlo, int whi, bool dag, unsigned seed) {
    std::mt19937 rng(seed);
    std::uniform_real_distribution<double> coin(0.0, 1.0);
    std::uniform_int_distribution<int> weight(wlo, whi);
    vector<Edge> edges;
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v) {
            if (u == v) continue;
            if (!directed && v < u) continue; // each undirected pair once
            if (dag && v <= u) continue;       // DAG: forward edges only
            if (coin(rng) < density) {
                int w = weighted ? weight(rng) : 1;
                edges.emplace_back(u, v, w);
            }
        }
    return edges;
}

void printEdgeList(int n, const vector<Edge>& edges) {
    std::cout << "# " << n << " vertices, " << edges.size() << " edges (u v w)\n";
    for (auto& [u, v, w] : edges) std::cout << u << " " << v << " " << w << "\n";
}

void printAdjMatrix(int n, const vector<Edge>& edges, bool directed) {
    vector<vector<int>> m(n, vector<int>(n, 0)); // 0 = no edge
    for (auto& [u, v, w] : edges) {
        m[u][v] = w;
        if (!directed) m[v][u] = w;
    }
    std::cout << "    ";
    for (int j = 0; j < n; ++j) std::cout << std::setw(3) << j << " ";
    std::cout << "\n";
    for (int i = 0; i < n; ++i) {
        std::cout << std::setw(3) << i << " ";
        for (int j = 0; j < n; ++j) std::cout << std::setw(3) << m[i][j] << " ";
        std::cout << "\n";
    }
}

void printDot(int n, const vector<Edge>& edges, bool directed) {
    std::string kind = directed ? "digraph" : "graph";
    std::string conn = directed ? "->" : "--";
    std::cout << kind << " G {\n";
    for (int v = 0; v < n; ++v) std::cout << "  " << v << ";\n";
    for (auto& [u, v, w] : edges)
        std::cout << "  " << u << " " << conn << " " << v << " [label=\"" << w << "\"];\n";
    std::cout << "}\n";
}

int main() {
    int n = 6;
    bool directed = false;
    auto edges = generate(n, 0.45, directed, /*weighted=*/true, 1, 9, /*dag=*/false, 7);

    std::cout << "=== Edge list ===\n";
    printEdgeList(n, edges);
    std::cout << "\n=== Adjacency matrix (0 = no edge) ===\n";
    printAdjMatrix(n, edges, directed);
    std::cout << "\n=== Graphviz DOT ===\n";
    printDot(n, edges, directed);
    return 0;
}
