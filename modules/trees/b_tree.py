"""
B-Tree  (CSC310 Module 5 - Advanced Trees)
==========================================

A B-tree of minimum degree t keeps every node between t-1 and 2t-1 keys (the root
may have fewer), and all leaves at the same depth -- so it stays shallow even for
huge data sets, which is why databases and file systems use it.  Insertion splits
any full (2t-1 key) node on the way down, so the height only grows when the root
splits.

Search / insert run in O(t log_t n).
"""


class BTreeNode:
    def __init__(self, leaf):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:
    def __init__(self, t):
        if t < 2:
            raise ValueError("minimum degree t must be >= 2")
        self.t = t
        self.root = BTreeNode(leaf=True)

    # --- search ---
    def search(self, key, node=None):
        node = node or self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return True
        if node.leaf:
            return False
        return self.search(key, node.children[i])

    # --- insert ---
    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:      # root full: grow height
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_nonfull(new_root, key)
        else:
            self._insert_nonfull(root, key)

    def _split_child(self, parent, i):
        t = self.t
        full = parent.children[i]
        new = BTreeNode(leaf=full.leaf)
        mid = full.keys[t - 1]                     # median moves up to the parent
        new.keys = full.keys[t:]                   # right half -> new node
        full.keys = full.keys[:t - 1]              # left half stays
        if not full.leaf:
            new.children = full.children[t:]
            full.children = full.children[:t]
        parent.children.insert(i + 1, new)
        parent.keys.insert(i, mid)

    def _insert_nonfull(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_nonfull(node.children[i], key)

    # --- helpers for display / checking ---
    def inorder(self, node=None, out=None):
        out = out if out is not None else []
        node = node or self.root
        for i, k in enumerate(node.keys):
            if not node.leaf:
                self.inorder(node.children[i], out)
            out.append(k)
        if not node.leaf:
            self.inorder(node.children[-1], out)
        return out

    def print_levels(self):
        level = [self.root]
        depth = 0
        while level:
            print(f"  level {depth}: " +
                  "  ".join("[" + ",".join(map(str, n.keys)) + "]" for n in level))
            nxt = []
            for n in level:
                nxt.extend(n.children)
            level = nxt
            depth += 1


def main():
    t = 3                                          # nodes hold 2..5 keys
    tree = BTree(t)
    keys = [10, 20, 5, 6, 12, 30, 7, 17, 3, 8, 25, 40, 1, 22, 11, 9, 33, 18]
    print(f"B-tree (minimum degree t={t}); inserting:")
    print(f"  {keys}\n")
    for k in keys:
        tree.insert(k)

    print("Tree by level (each [..] is one node):")
    tree.print_levels()

    order = tree.inorder()
    print(f"\nIn-order keys: {order}")
    print(f"In-order is sorted: {order == sorted(keys)}")
    print(f"search(17): {tree.search(17)},  search(99): {tree.search(99)}")


if __name__ == "__main__":
    main()
