// Strongly Connected Components - Kosaraju's Algorithm  (CSC310 Module 7)
// =====================================================================
//
// Build:  g++ -std=c++17 -O2 scc_kosaraju.cpp -o scc_kosaraju && ./scc_kosaraju
//
// Time: O(|V| + |E|).
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using std::map;
using std::string;
using std::vector;

map<string, vector<string>> adj, transpose_;
std::set<string> visited;
vector<string> finishStack;

void dfs1(const string& u) {
    visited.insert(u);
    for (const auto& v : adj[u])
        if (!visited.count(v)) dfs1(v);
    finishStack.push_back(u);          // record finish order
}

void dfs2(const string& u, vector<string>& comp) {
    visited.insert(u);
    comp.push_back(u);
    for (const auto& v : transpose_[u])
        if (!visited.count(v)) dfs2(v, comp);
}

int main() {
    // CLRS Fig. 22.9 directed graph.
    adj = {
        {"a", {"b"}}, {"b", {"c", "e", "f"}}, {"c", {"d", "g"}},
        {"d", {"c", "h"}}, {"e", {"a", "f"}}, {"f", {"g"}},
        {"g", {"f", "h"}}, {"h", {"h"}},
    };

    for (const auto& [u, nbrs] : adj) {        // 1. finish order on G
        if (!visited.count(u)) dfs1(u);
    }
    for (const auto& [u, nbrs] : adj)          // 2. transpose
        for (const auto& v : nbrs)
            transpose_[v].push_back(u);

    visited.clear();                           // 3. DFS transpose in reverse finish order
    vector<vector<string>> comps;
    for (auto it = finishStack.rbegin(); it != finishStack.rend(); ++it) {
        if (!visited.count(*it)) {
            vector<string> comp;
            dfs2(*it, comp);
            std::sort(comp.begin(), comp.end());
            comps.push_back(comp);
        }
    }

    std::cout << "Strongly connected components (" << comps.size() << "):\n";
    for (const auto& c : comps) {
        std::cout << "  {";
        for (size_t i = 0; i < c.size(); ++i)
            std::cout << c[i] << (i + 1 < c.size() ? ", " : "");
        std::cout << "}\n";
    }
    return 0;
}
