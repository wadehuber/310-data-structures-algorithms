"""
BinaryTreeNode represents a node in a binary tree with a left and
right child.

1-1 conversion of heaps/linkedheap/BinaryTreeNode.java
"""


class BinaryTreeNode:

    def __init__(self, obj):
        # Creates a new tree node with the specified data.
        self.element = obj
        self.left = None
        self.right = None

    def num_children(self):
        # Returns the number of non-null children of this node.
        children = 0

        if self.left is not None:
            children = 1 + self.left.num_children()

        if self.right is not None:
            children = children + 1 + self.right.num_children()

        return children

    def get_element(self):
        # Return the element at this node.
        return self.element

    def get_right(self):
        # Return the right child of this node.
        return self.right

    def set_right(self, node):
        # Sets the right child of this node.
        self.right = node

    def get_left(self):
        # Return the left child of this node.
        return self.left

    def set_left(self, node):
        # Sets the left child of this node.
        self.left = node
