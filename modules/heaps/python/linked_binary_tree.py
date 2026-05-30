"""
LinkedBinaryTree implements a binary tree.

1-1 conversion of heaps/linkedheap/LinkedBinaryTree.java
(the iterator's concurrent-modification machinery is simplified to a
plain in-order generator, which is the Pythonic equivalent).
"""

from binary_tree_node import BinaryTreeNode
from exceptions import EmptyCollectionException, ElementNotFoundException


class LinkedBinaryTree:

    def __init__(self, element=None):
        # Creates an empty binary tree, or one with the given root element.
        self.mod_count = 0
        if element is None:
            self.root = None
        else:
            self.root = BinaryTreeNode(element)

    def get_root_element(self):
        # Returns a reference to the element at the root.
        if self.root is None:
            raise EmptyCollectionException("LinkedBinaryTree")

        return self.root.get_element()

    def get_root_node(self):
        # Returns a reference to the node at the root.
        if self.root is None:
            raise EmptyCollectionException("LinkedBinaryTree")

        return self.root

    def get_left(self):
        # Returns the left subtree of the root of this tree.
        if self.root is None:
            raise EmptyCollectionException("LinkedBinaryTree - getLeft() -")

        result = LinkedBinaryTree()
        result.root = self.root.get_left()

        return result

    def get_right(self):
        # Returns the right subtree of the root of this tree.
        if self.root is None:
            raise EmptyCollectionException("LinkedBinaryTree - getRight() -")

        result = LinkedBinaryTree()
        result.root = self.root.get_right()

        return result

    def is_empty(self):
        # Returns true if this binary tree is empty and false otherwise.
        return self.root is None

    def size(self):
        # Returns the integer size of this tree.
        if self.root is None:
            return 0

        return self.root.num_children() + 1

    def get_height(self):
        # Returns the height of this tree.
        return self.height(self.root) - 1

    def height(self, node):
        # Returns the height of the specified node.
        result = 0
        if node is not None:
            result = max(self.height(node.get_left()),
                         self.height(node.get_right())) + 1

        return result

    def contains(self, target_element):
        # Returns true if this tree contains a matching element.
        try:
            self.find(target_element)
            found = True
        except Exception:
            found = False

        return found

    def find(self, target_element):
        # Returns a reference to the specified target element if found.
        current = self.find_node(target_element, self.root)

        if current is None:
            raise ElementNotFoundException("LinkedBinaryTree")

        return current.get_element()

    def find_node(self, target_element, next):
        # Returns the node holding the target element, or None.
        if next is None:
            return None

        if next.get_element() == target_element:
            return next

        temp = self.find_node(target_element, next.get_left())

        if temp is None:
            temp = self.find_node(target_element, next.get_right())

        return temp

    def __str__(self):
        # Returns an in-order string representation of this binary tree.
        temp_list = []
        self.in_order(self.root, temp_list)

        ret = ""

        for element in temp_list:
            ret += str(element) + " "

        return ret

    def __iter__(self):
        # Returns an in-order iterator over this binary tree.
        temp_list = []
        self.in_order(self.root, temp_list)
        return iter(temp_list)

    def in_order(self, node, temp_list):
        # Performs a recursive in-order traversal.
        if node is not None:
            self.in_order(node.get_left(), temp_list)
            temp_list.append(node.get_element())
            self.in_order(node.get_right(), temp_list)
