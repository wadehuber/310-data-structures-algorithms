"""
LinkedHeap implements a min heap on top of a LinkedBinaryTree.

1-1 conversion of heaps/linkedheap/LinkedHeap.java
(Java's Comparable.compareTo(x) < 0 becomes Python's "a < b").
"""

from linked_binary_tree import LinkedBinaryTree
from heap_node import HeapNode
from exceptions import EmptyCollectionException


class LinkedHeap(LinkedBinaryTree):

    def __init__(self):
        super().__init__()
        self.last_node = None

    def add_element(self, obj):
        # Adds the specified element to this heap in the appropriate position.
        node = HeapNode(obj)

        if self.root is None:
            self.root = node
        else:
            next_parent = self.get_next_parent_add()  # keep heap structure
            # Determine which child
            if next_parent.get_left() is None:    # no children
                next_parent.set_left(node)
            else:                                 # one child - the left node
                next_parent.set_right(node)

            node.set_parent(next_parent)
        self.last_node = node
        self.mod_count += 1

        if self.size() > 1:
            self.heapify_add()  # keep the heap ordering

    def get_next_parent_add(self):
        # Returns the node that will be the parent of the new node.
        result = self.last_node

        # Get to the left sub-tree or the root
        while (result is not self.root) and (result.get_parent().get_left() is not result):
            result = result.get_parent()

        if result is not self.root:
            # Go to the parent's right subtree
            if result.get_parent().get_right() is None:
                # Parent has no right child, so parent is the new parent
                result = result.get_parent()
            else:
                # Get parent's right child
                result = result.get_parent().get_right()
                # Go all the way to the left
                while result.get_left() is not None:
                    result = result.get_left()
        else:
            # Tree is full so go all the way to the left (start a new row of leaves)
            while result.get_left() is not None:
                result = result.get_left()

        return result

    def heapify_add(self):
        # Reorders this heap after adding a node.
        next = self.last_node

        temp = next.get_element()

        while (next is not self.root) and (temp < next.get_parent().get_element()):
            next.set_element(next.get_parent().get_element())
            next = next.parent
        next.set_element(temp)

    def remove_min(self):
        # Remove and return the element with the lowest value in this heap.
        if self.is_empty():
            raise EmptyCollectionException("LinkedHeap")

        min_element = self.root.get_element()

        # If the size is 1 the heap will be empty
        if self.size() == 1:
            self.root = None
            self.last_node = None
        else:
            # Get the new last node
            new_last = self.get_new_last_node()

            # Check which child the old last node is & set to null
            if self.last_node.get_parent().get_left() is self.last_node:
                self.last_node.get_parent().set_left(None)
            else:
                self.last_node.get_parent().set_right(None)

            self.root.set_element(self.last_node.get_element())
            self.last_node = new_last
            self.heapify_remove()
        self.mod_count += 1
        return min_element

    def heapify_remove(self):
        # Reorders this heap after removing the root element.
        node = self.root
        left = node.get_left()
        right = node.get_right()

        if (left is None) and (right is None):
            # no children
            next = None
        elif right is None:
            # one child
            next = left
        elif left.get_element() < right.get_element():
            # two children, left is smaller
            next = left
        else:
            # two children, right is smaller
            next = right

        temp = node.get_element()
        while (next is not None) and (next.get_element() < temp):
            node.set_element(next.get_element())
            node = next
            left = node.get_left()
            right = node.get_right()

            if (left is None) and (right is None):
                next = None
            elif right is None:
                next = left
            elif left.get_element() < right.get_element():
                next = left
            else:
                next = right
        node.set_element(temp)

    def get_new_last_node(self):
        # Returns the node that will be the new last node after a remove.
        new_last_node = self.last_node

        while (new_last_node is not self.root) and (new_last_node.get_parent().get_left() is new_last_node):
            new_last_node = new_last_node.get_parent()

        if new_last_node is not self.root:
            new_last_node = new_last_node.get_parent().get_left()

        while new_last_node.get_right() is not None:
            new_last_node = new_last_node.get_right()

        return new_last_node

    def find_min(self):
        # Returns the element with the lowest value in this heap.
        if self.is_empty():
            raise EmptyCollectionException("LinkedHeap")

        return self.root.get_element()
