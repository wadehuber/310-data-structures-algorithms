# Binary Trees & Balanced Trees

Code for **Module 5 — Binary, Search & Balanced Trees** (CLRS Ch. 12, 13, 18).
After a review of binary trees and BSTs, the module covers rotations and the
self-balancing trees that keep operations O(log n): AVL, Red-Black, and B-Trees.

## Tree Review (from CSC205)

The `binarytreereview` package contains binary-tree and BST examples from the
Java Foundations textbook, covered in CSC205.

### Binary Trees

- `TreeBuildingExample.java` — building a BinaryTree with the LinkedBinaryTree class
- [Video: Overview of Trees](https://youtu.be/4VXGE6cNIvE) (13:49)
- [Video: Implementing Trees with Arrays](https://youtu.be/zuWvrqcZwuU) (8:58)
- [Video: Tree Traversals](https://youtu.be/OXy4pLq_XZs) (5:04)

### Binary Search Trees

- `BSTExample.java` — building a BST with the LinkedBinarySearchTree class
- [VIDEO: BSTs Part 1 — Overview](https://youtu.be/Y2kB1DLADZ4) (9:34)
- [VIDEO: BSTs Part 2 — Adding Elements](https://youtu.be/h5XnGwMhBJk) (8:56)
- [VIDEO: BSTs Part 3 — Removing Elements](https://youtu.be/XCF0-lXBtv4) (12:13)

### Rotations

- [Video: Tree Rotations](https://youtu.be/pMfoyc6zmZo) (4:29): left & right rotations

## Advanced Trees (Module 5B)

| Topic | Language(s) | Notes |
|-------|--------|-------------|-------|
| B-Tree (minimum degree t) | Python, C++ | Insert with node splitting, search, in-order; prints the tree level by level. Stays shallow and balanced. |
| Tree validators | Python | `is_valid_bst`, `is_height_balanced` (AVL property), and the five red-black properties, each with a PASS/FAIL demo. |
| AVL tree | Scheme | Esoteric language, different key sequence; purely functional insert with LL/RR/LR/RL rebalancing. |

## What each shows

- **B-Tree** — the multi-way balanced tree used for on-disk data: every node
  holds t−1..2t−1 keys and all leaves sit at the same depth, so the tree is wide
  and short. Splitting a full node on the way down is what keeps it balanced.
- **Validators** — confirm the BST ordering (via value bounds), the AVL
  height-balance invariant, and the red-black properties (root black, no red-red,
  equal black-heights). Run your Project 2 tree through these to check it.
- **AVL tree** — a self-balancing BST: after each insert the balance factor is
  checked and one of four rotation cases restores the ±1 invariant.

## Running

```bash
python3 b_tree.py
g++ -std=c++17 -O2 b_tree.cpp -o b_tree && ./b_tree

python3 tree_validators.py

guile avl_tree.scm        # Scheme (GNU Guile)
```

## Where each ties back to the notes

- *Binary Trees / BSTs / Traversals* → `binarytreereview/` (CSC205 review)
- *Rotations & AVL Trees* → `avl_tree.scm`
- *Red-Black properties / balance* → `tree_validators.py`
- *B-Trees* → `b_tree.py`, `b_tree.cpp`
