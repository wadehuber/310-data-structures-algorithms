// HeapNode represents a binary tree node with a parent pointer for use
// in heaps.
//
// 1-1 conversion of heaps/linkedheap/HeapNode.java
#ifndef HEAP_NODE_HPP
#define HEAP_NODE_HPP

#include "BinaryTreeNode.hpp"

template <typename T>
class HeapNode : public BinaryTreeNode<T>
{
public:
    HeapNode<T>* parent;

    // Creates a new heap node with the specified data.
    HeapNode(T obj) : BinaryTreeNode<T>(obj)
    {
        parent = nullptr;
    }

    // Return the parent of this node.
    HeapNode<T>* getParent() { return parent; }

    // Sets the element stored at this node.
    void setElement(T obj) { this->element = obj; }

    // Sets the parent of this node.
    void setParent(HeapNode<T>* node) { parent = node; }
};

#endif
