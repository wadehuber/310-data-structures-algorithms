// PriorityQueue implements a priority queue using a heap.
//
// 1-1 conversion of priorityqueue/PriorityQueue.java
#ifndef PRIORITY_QUEUE_HPP
#define PRIORITY_QUEUE_HPP

#include "LinkedHeap.hpp"
#include "PrioritizedObject.hpp"

template <typename T>
class PriorityQueue
{
private:
    LinkedHeap<PrioritizedObject<T>> pqueue;

public:
    // Creates an empty priority queue.
    PriorityQueue() {}

    // Adds the given element to this PriorityQueue.
    void addElement(T object, int priority)
    {
        PrioritizedObject<T> obj(object, priority);
        pqueue.addElement(obj);
    }

    // Removes and returns the next highest priority element.
    T removeNext()
    {
        PrioritizedObject<T> obj = pqueue.removeMin();
        return obj.getElement();
    }

    int size() { return pqueue.size(); }

    bool isEmpty() { return pqueue.isEmpty(); }
};

#endif
