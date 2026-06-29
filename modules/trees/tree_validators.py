"""
Tree Validators  (CSC310 Module 5 - Advanced Trees)
==================================================

These functions CHECK whether a tree has a given property; they do NOT 
build or balance a tree.  This validator verifies output you produced
some other way, which makes it a handy self-test for that project.

Includes:
  - is_valid_bst        : left < node <= right everywhere (via value bounds)
  - is_height_balanced  : |height(left) - height(right)| <= 1 at every node (AVL)
  - validate_red_black  : the five red-black properties
"""

class Node:
    def __init__(self, key, left=None, right=None, color=None):
        self.key = key
        self.left = left
        self.right = right
        self.color = color          # "R" or "B" for red-black trees


# ---------- BST property ----------
def is_valid_bst(node, lo=float("-inf"), hi=float("inf")):
    if node is None:
        return True, "ok"
    if not (lo <= node.key <= hi):
        return False, f"node {node.key} violates bounds ({lo}, {hi})"
    ok, msg = is_valid_bst(node.left, lo, node.key)
    if not ok:
        return ok, msg
    return is_valid_bst(node.right, node.key, hi)


# ---------- height balance (AVL property) ----------
def height(node):
    return -1 if node is None else 1 + max(height(node.left), height(node.right))

def is_height_balanced(node):
    if node is None:
        return True
    if abs(height(node.left) - height(node.right)) > 1:
        return False
    return is_height_balanced(node.left) and is_height_balanced(node.right)


# ---------- red-black properties ----------
def validate_red_black(root):
    if root is not None and root.color != "B":
        return False, "the root must be black"

    bad = [None]

    def black_height(node):
        if node is None:
            return 1                       # NIL leaves are black, height 1
        if bad[0]:
            return 0
        if node.color == "R":
            for c in (node.left, node.right):
                if c is not None and c.color == "R":
                    bad[0] = f"red node {node.key} has a red child {c.key}"
                    return 0
        lh = black_height(node.left)
        rh = black_height(node.right)
        if lh != rh and not bad[0]:
            bad[0] = f"black-height mismatch at node {node.key} ({lh} vs {rh})"
        return lh + (1 if node.color == "B" else 0)

    black_height(root)
    return (bad[0] is None), (bad[0] or "valid red-black tree")


def report(title, result):
    ok, msg = result
    print(f"  {title}: {'PASS' if ok else 'FAIL'} - {msg}")


def main():
    print("== BST property ==")
    valid_bst = Node(8, Node(3, Node(1), Node(6)), Node(10, None, Node(14)))
    bad_bst = Node(8, Node(3, Node(1), Node(9)), Node(10))   # 9 sits left of 8
    report("a correct BST", is_valid_bst(valid_bst))
    report("9 placed left of 8", is_valid_bst(bad_bst))

    print("\n== Height balance (AVL property) ==")
    chain = Node(1, None, Node(2, None, Node(3, None, Node(4))))   # degenerate
    print(f"  balanced tree : {'PASS' if is_height_balanced(valid_bst) else 'FAIL'}")
    print(f"  right-leaning chain : {'PASS' if is_height_balanced(chain) else 'FAIL'}")

    print("\n== Red-black properties ==")
    good_rb = Node(2, Node(1, color="R"), Node(3, color="R"), color="B")
    bad_rb = Node(2, Node(1, Node(0, color="R"), color="R"), color="B")  # red-red
    report("valid red-black tree", validate_red_black(good_rb))
    report("red node with red child", validate_red_black(bad_rb))


if __name__ == "__main__":
    main()
