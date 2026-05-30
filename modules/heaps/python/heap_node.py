"""
HeapNode represents a binary tree node with a parent pointer for use
in heaps.

1-1 conversion of heaps/linkedheap/HeapNode.java
"""

from binary_tree_node import BinaryTreeNode


class HeapNode(BinaryTreeNode):

    def __init__(self, obj):
        # Creates a new heap node with the specified data.
        super().__init__(obj)
        self.parent = None

    def get_parent(self):
        # Return the parent of this node.
        return self.parent

    def set_element(self, obj):
        # Sets the element stored at this node.
        self.element = obj

    def set_parent(self, node):
        # Sets the parent of this node.
        self.parent = node
