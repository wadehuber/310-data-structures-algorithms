"""
Exception types used by the heap classes.

1-1 conversion of the Java classes in
heaps/linkedheap/exceptions/.
"""


class EmptyCollectionException(Exception):
    """Represents the situation in which a collection is empty."""

    def __init__(self, collection):
        super().__init__("The " + collection + " is empty.")


class ElementNotFoundException(Exception):
    """Represents the situation in which a target element is not found."""

    def __init__(self, collection):
        super().__init__("The target is not in the " + collection + ".")
