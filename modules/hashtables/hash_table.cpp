// Separate-Chaining Hash Table with Resizing  (CSC310 Module 4B - Hashing)
// =======================================================================
//
// Separate chaining: each slot holds a list of entries.  When the load factor
// n/m exceeds a threshold, the table doubles and every entry is rehashed
// (amortized O(1) per operation).  Keys are strings, values are ints.
//
// Build:  g++ -std=c++17 -O2 hash_table.cpp -o hash_table && ./hash_table
#include <iostream>
#include <list>
#include <string>
#include <utility>
#include <vector>

class HashTable {
    std::vector<std::list<std::pair<std::string, int>>> buckets;
    size_t n = 0;                         // number of stored entries
    const double MAX_LOAD = 0.75;

    size_t hash(const std::string& key) const {
        unsigned long h = 0;              // polynomial string hash, then division
        for (unsigned char c : key) h = h * 31 + c;
        return h % buckets.size();
    }

    void resize(size_t newCap) {
        std::vector<std::list<std::pair<std::string, int>>> old = std::move(buckets);
        buckets.assign(newCap, {});
        n = 0;
        for (auto& chain : old)
            for (auto& [k, v] : chain) put(k, v);   // rehash into the bigger table
    }

public:
    explicit HashTable(size_t cap = 4) : buckets(cap) {}

    void put(const std::string& key, int value) {
        auto& chain = buckets[hash(key)];
        for (auto& [k, v] : chain)
            if (k == key) { v = value; return; }     // update existing key
        chain.emplace_back(key, value);
        ++n;
        if ((double)n / buckets.size() > MAX_LOAD) resize(buckets.size() * 2);
    }

    bool get(const std::string& key, int& out) const {
        for (auto& [k, v] : buckets[hash(key)])
            if (k == key) { out = v; return true; }
        return false;
    }

    bool remove(const std::string& key) {
        auto& chain = buckets[hash(key)];
        for (auto it = chain.begin(); it != chain.end(); ++it)
            if (it->first == key) { chain.erase(it); --n; return true; }
        return false;
    }

    size_t size() const { return n; }
    size_t capacity() const { return buckets.size(); }
    double load() const { return (double)n / buckets.size(); }
};

int main() {
    HashTable t(4);                       // small so we can watch it grow
    const char* names[] = {"Andy", "Maribel", "Zoey", "Julie", "Ann", "Stephen"};
    int age = 20;
    for (auto nm : names) {
        t.put(nm, age++);
        std::cout << "put " << nm << " -> capacity now " << t.capacity()
                  << ", load " << t.load() << "\n";
    }

    int v;
    std::cout << "\nget Zoey: " << (t.get("Zoey", v) ? std::to_string(v) : "absent") << "\n";
    t.remove("Zoey");
    std::cout << "after remove Zoey, get Zoey: "
              << (t.get("Zoey", v) ? std::to_string(v) : "absent") << "\n";
    std::cout << "size=" << t.size() << ", capacity=" << t.capacity() << "\n";
    return 0;
}
