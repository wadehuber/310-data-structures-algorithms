// Offline Caching: Belady's MIN vs. LRU  (CSC310 Module 12 - Greedy Algorithms)
// ============================================================================
//
// Belady's MIN (offline, optimal): on a miss with a full cache, evict the page
// whose next use is farthest in the future.  LRU (online) evicts the
// least-recently-used page.  MIN is provably optimal, so it never has more
// misses than LRU.
//
// Build:  g++ -std=c++17 -O2 offline_caching.cpp -o offline_caching && ./offline_caching

#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

using std::vector;

static void printCache(const vector<int>& c) {
    std::cout << "cache=[";
    for (size_t i = 0; i < c.size(); ++i)
        std::cout << c[i] << (i + 1 < c.size() ? ", " : "");
    std::cout << "]\n";
}

// Belady's MIN: evict the page whose next use is farthest in the future.
int belady(const vector<int>& req, int k) {
    vector<int> cache;
    int misses = 0;
    for (size_t t = 0; t < req.size(); ++t) {
        int page = req[t];
        if (std::find(cache.begin(), cache.end(), page) != cache.end()) {
            std::cout << "  request " << page << "  hit            ";
            printCache(cache);
            continue;
        }
        ++misses;
        if ((int)cache.size() < k) {
            cache.push_back(page);
            std::cout << "  request " << page << "  miss/load      ";
            printCache(cache);
        } else {
            int victimIdx = 0, farthest = -1;
            for (size_t c = 0; c < cache.size(); ++c) {
                int nextUse = std::numeric_limits<int>::max();
                for (size_t j = t + 1; j < req.size(); ++j)
                    if (req[j] == cache[c]) { nextUse = (int)j; break; }
                if (nextUse > farthest) { farthest = nextUse; victimIdx = (int)c; }
            }
            std::cout << "  request " << page << "  miss/evict " << cache[victimIdx] << "  ";
            cache[victimIdx] = page;
            printCache(cache);
        }
    }
    return misses;
}

// LRU: cache ordered oldest-use -> newest-use; evict the front on a full miss.
int lru(const vector<int>& req, int k) {
    vector<int> cache;
    int misses = 0;
    for (int page : req) {
        auto it = std::find(cache.begin(), cache.end(), page);
        if (it != cache.end()) {
            cache.erase(it);
            cache.push_back(page);
            std::cout << "  request " << page << "  hit            ";
            printCache(cache);
            continue;
        }
        ++misses;
        if ((int)cache.size() == k) {
            std::cout << "  request " << page << "  miss/evict " << cache.front() << "  ";
            cache.erase(cache.begin());
            cache.push_back(page);
        } else {
            cache.push_back(page);
            std::cout << "  request " << page << "  miss/load      ";
        }
        printCache(cache);
    }
    return misses;
}

int main() {
    vector<int> req = {1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5};
    int k = 3;

    std::cout << "Request sequence: ";
    for (int p : req) std::cout << p << " ";
    std::cout << "\nCache size k = " << k << "\n\n";

    std::cout << "=== Belady's MIN (optimal, offline) ===\n";
    int bm = belady(req, k);
    std::cout << "\n=== LRU (online) ===\n";
    int lm = lru(req, k);

    std::cout << "\nBelady misses = " << bm << ", LRU misses = " << lm << "\n";
    std::cout << "Belady is optimal, so it never has more misses than LRU.\n";
    return 0;
}
