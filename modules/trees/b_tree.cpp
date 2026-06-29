// B-Tree  (CSC310 Module 5 - Advanced Trees)
// ==========================================
//
// Minimum degree t: every node holds t-1..2t-1 keys (root may hold fewer), all
// leaves at the same depth.  Insertion splits any full node on the way down.
//
// Build:  g++ -std=c++17 -O2 b_tree.cpp -o b_tree && ./b_tree
#include <algorithm>
#include <iostream>
#include <vector>

struct BTreeNode {
    std::vector<int> keys;
    std::vector<BTreeNode*> children;
    bool leaf;
    explicit BTreeNode(bool lf) : leaf(lf) {}
};

class BTree {
    int t;
    BTreeNode* root;

    void splitChild(BTreeNode* parent, int i) {
        BTreeNode* full = parent->children[i];
        BTreeNode* node = new BTreeNode(full->leaf);
        int mid = full->keys[t - 1];                        // median moves up
        node->keys.assign(full->keys.begin() + t, full->keys.end());
        full->keys.resize(t - 1);
        if (!full->leaf) {
            node->children.assign(full->children.begin() + t, full->children.end());
            full->children.resize(t);
        }
        parent->children.insert(parent->children.begin() + i + 1, node);
        parent->keys.insert(parent->keys.begin() + i, mid);
    }

    void insertNonFull(BTreeNode* node, int key) {
        int i = (int)node->keys.size() - 1;
        if (node->leaf) {
            node->keys.push_back(0);
            while (i >= 0 && key < node->keys[i]) { node->keys[i + 1] = node->keys[i]; --i; }
            node->keys[i + 1] = key;
        } else {
            while (i >= 0 && key < node->keys[i]) --i;
            ++i;
            if ((int)node->children[i]->keys.size() == 2 * t - 1) {
                splitChild(node, i);
                if (key > node->keys[i]) ++i;
            }
            insertNonFull(node->children[i], key);
        }
    }

    bool search(BTreeNode* node, int key) {
        int i = 0;
        while (i < (int)node->keys.size() && key > node->keys[i]) ++i;
        if (i < (int)node->keys.size() && node->keys[i] == key) return true;
        return node->leaf ? false : search(node->children[i], key);
    }

    void inorder(BTreeNode* node, std::vector<int>& out) {
        for (size_t i = 0; i < node->keys.size(); ++i) {
            if (!node->leaf) inorder(node->children[i], out);
            out.push_back(node->keys[i]);
        }
        if (!node->leaf) inorder(node->children.back(), out);
    }

public:
    explicit BTree(int t_) : t(t_), root(new BTreeNode(true)) {}

    void insert(int key) {
        if ((int)root->keys.size() == 2 * t - 1) {           // root full: grow height
            BTreeNode* newRoot = new BTreeNode(false);
            newRoot->children.push_back(root);
            splitChild(newRoot, 0);
            root = newRoot;
        }
        insertNonFull(root, key);
    }

    bool search(int key) { return search(root, key); }
    std::vector<int> inorder() { std::vector<int> out; inorder(root, out); return out; }

    void printLevels() {
        std::vector<BTreeNode*> level{root};
        int depth = 0;
        while (!level.empty()) {
            std::cout << "  level " << depth << ": ";
            for (auto* n : level) {
                std::cout << "[";
                for (size_t i = 0; i < n->keys.size(); ++i)
                    std::cout << n->keys[i] << (i + 1 < n->keys.size() ? "," : "");
                std::cout << "]  ";
            }
            std::cout << "\n";
            std::vector<BTreeNode*> nxt;
            for (auto* n : level)
                for (auto* c : n->children) nxt.push_back(c);
            level = nxt;
            ++depth;
        }
    }
};

int main() {
    int t = 3;
    BTree tree(t);
    std::vector<int> keys = {10, 20, 5, 6, 12, 30, 7, 17, 3, 8, 25, 40, 1, 22, 11, 9, 33, 18};
    std::cout << "B-tree (minimum degree t=" << t << "); inserting " << keys.size() << " keys\n\n";
    for (int k : keys) tree.insert(k);

    std::cout << "Tree by level (each [..] is one node):\n";
    tree.printLevels();

    auto order = tree.inorder();
    bool sorted = std::is_sorted(order.begin(), order.end());
    std::cout << "\nIn-order keys:";
    for (int k : order) std::cout << " " << k;
    std::cout << "\nIn-order is sorted: " << (sorted ? "true" : "false") << "\n";
    std::cout << "search(17): " << (tree.search(17) ? "true" : "false")
              << ",  search(99): " << (tree.search(99) ? "true" : "false") << "\n";
    return 0;
}
