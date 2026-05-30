"""
PriorityQueue implements a priority queue using a heap.

1-1 conversion of priorityqueue/PriorityQueue.java
"""

from linked_heap import LinkedHeap
from prioritized_object import PrioritizedObject


class PriorityQueue:

    def __init__(self):
        # Creates an empty priority queue.
        self.pqueue = LinkedHeap()

    def add_element(self, object, priority):
        # Adds the given element to this PriorityQueue.
        obj = PrioritizedObject(object, priority)
        self.pqueue.add_element(obj)

    def remove_next(self):
        # Removes and returns the next highest priority element.
        obj = self.pqueue.remove_min()
        return obj.get_element()

    def size(self):
        return self.pqueue.size()

    def is_empty(self):
        return self.pqueue.is_empty()
