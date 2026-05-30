"""
PrioritizedObject represents a node in a priority queue containing a
comparable object, arrival order, and a priority value.

1-1 conversion of priorityqueue/PrioritizedObject.java
(Java's compareTo is mirrored, and __lt__ delegates to it so the heap's
"a < b" works exactly as the Java heap's compareTo(...) < 0).
"""


class PrioritizedObject:

    next_order = 0  # static field shared across all instances

    def __init__(self, element, priority):
        # Creates a new PrioritizedObject with the specified data.
        self.element = element
        self.priority = priority
        self.arrival_order = PrioritizedObject.next_order
        PrioritizedObject.next_order += 1

    def get_element(self):
        # Returns the element in this node.
        return self.element

    def get_priority(self):
        # Returns the priority value for this node.
        return self.priority

    def get_arrival_order(self):
        # Returns the arrival order for this node.
        return self.arrival_order

    def __str__(self):
        # Returns a string representation for this node.
        return str(self.element) + "  " + str(self.priority) + "  " + str(self.arrival_order)

    def compare_to(self, obj):
        # Returns 1 if this object has higher priority than the given object
        # and -1 otherwise.

        # Give preference to PrioritizedObject with higher priority
        if self.priority > obj.get_priority():
            result = 1
        elif self.priority < obj.get_priority():
            result = -1
        # If the priorities are equal, first come first served
        elif self.arrival_order > obj.get_arrival_order():
            result = 1
        else:
            result = -1

        return result

    def __lt__(self, obj):
        # The heap orders elements with "a < b"; defer to compare_to.
        return self.compare_to(obj) < 0
