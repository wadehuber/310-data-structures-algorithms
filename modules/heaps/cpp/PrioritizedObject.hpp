// PrioritizedObject represents a node in a priority queue containing a
// comparable object, arrival order, and a priority value.
//
// 1-1 conversion of priorityqueue/PrioritizedObject.java
// (Java's compareTo is mirrored, and operator< defers to it so the heap's
// "a < b" behaves exactly like the Java heap's compareTo(...) < 0).
#ifndef PRIORITIZED_OBJECT_HPP
#define PRIORITIZED_OBJECT_HPP

#include <ostream>
#include <string>

template <typename T>
class PrioritizedObject
{
private:
    static int nextOrder;   // static field shared across all instances
    int priority;
    int arrivalOrder;
    T element;

public:
    // A default constructor is needed so this type can sit in the heap's
    // "T temp;" temporaries; it is never used to build a real queue node.
    PrioritizedObject() : priority(0), arrivalOrder(0), element() {}

    // Creates a new PrioritizedObject with the specified data.
    PrioritizedObject(T element, int priority)
    {
        this->element = element;
        this->priority = priority;
        arrivalOrder = nextOrder;
        nextOrder++;
    }

    // Returns the element in this node.
    T getElement() { return element; }

    // Returns the priority value for this node.
    int getPriority() { return priority; }

    // Returns the arrival order for this node.
    int getArrivalOrder() { return arrivalOrder; }

    // Returns 1 if this object has higher priority than the given object
    // and -1 otherwise.
    int compareTo(PrioritizedObject<T> obj)
    {
        int result;

        // Give preference to PrioritizedObject with higher priority
        if (priority > obj.getPriority())
            result = 1;
        else if (priority < obj.getPriority())
            result = -1;
        // If the priorities are equal, first come first served
        else if (arrivalOrder > obj.getArrivalOrder())
            result = 1;
        else
            result = -1;

        return result;
    }

    // The heap orders elements with "a < b"; defer to compareTo.
    bool operator<(PrioritizedObject<T> obj)
    {
        return compareTo(obj) < 0;
    }

    // Returns a string representation for this node.
    friend std::ostream& operator<<(std::ostream& os, const PrioritizedObject<T>& po)
    {
        os << po.element << "  " << po.priority << "  " << po.arrivalOrder;
        return os;
    }
};

template <typename T>
int PrioritizedObject<T>::nextOrder = 0;

#endif
