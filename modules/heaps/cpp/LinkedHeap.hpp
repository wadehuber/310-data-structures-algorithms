// LinkedHeap implements a min heap on top of a LinkedBinaryTree.
//
// 1-1 conversion of heaps/linkedheap/LinkedHeap.java
// (Java's Comparable.compareTo(x) < 0 becomes C++'s "a < b"; the casts
// to HeapNode become static_cast, and removed nodes are delete-d since
// C++ has no garbage collector).
#ifndef LINKED_HEAP_HPP
#define LINKED_HEAP_HPP

#include "LinkedBinaryTree.hpp"
#include "HeapNode.hpp"
#include "Exceptions.hpp"

template <typename T>
class LinkedHeap : public LinkedBinaryTree<T>
{
public:
    HeapNode<T>* lastNode;

    LinkedHeap() : LinkedBinaryTree<T>()
    {
        lastNode = nullptr;
    }

    // Adds the specified element to this heap in the appropriate position.
    void addElement(T obj)
    {
        HeapNode<T>* node = new HeapNode<T>(obj);

        if (this->root == nullptr)
            this->root = node;
        else
        {
            HeapNode<T>* nextParent = getNextParentAdd();  // keep heap structure
            // Determine which child
            if (nextParent->getLeft() == nullptr)   // no children
                nextParent->setLeft(node);
            else                                     // one child - the left node
                nextParent->setRight(node);

            node->setParent(nextParent);
        }
        lastNode = node;
        this->modCount++;

        if (this->size() > 1)
            heapifyAdd();  // keep the heap ordering
    }

    // Returns the node that will be the parent of the new node.
    HeapNode<T>* getNextParentAdd()
    {
        HeapNode<T>* result = lastNode;

        // Get to the left sub-tree or the root
        while ((result != this->root) && (result->getParent()->getLeft() != result))
            result = result->getParent();

        if (result != this->root)
            // Go to the parent's right subtree
            if (result->getParent()->getRight() == nullptr)
                // Parent has no right child, so parent is the new parent
                result = result->getParent();
            else
            {
                // Get parent's right child
                result = static_cast<HeapNode<T>*>(result->getParent()->getRight());
                // Go all the way to the left
                while (result->getLeft() != nullptr)
                    result = static_cast<HeapNode<T>*>(result->getLeft());
            }
        else
            // Tree is full so go all the way to the left (start a new row of leaves)
            while (result->getLeft() != nullptr)
                result = static_cast<HeapNode<T>*>(result->getLeft());

        return result;
    }

    // Reorders this heap after adding a node.
    void heapifyAdd()
    {
        T temp;
        HeapNode<T>* next = lastNode;

        temp = next->getElement();

        while ((next != this->root) &&
               (temp < next->getParent()->getElement()))
        {
            next->setElement(next->getParent()->getElement());
            next = next->parent;
        }
        next->setElement(temp);
    }

    // Remove and return the element with the lowest value in this heap.
    T removeMin()
    {
        if (this->isEmpty())
            throw EmptyCollectionException("LinkedHeap");

        T minElement = this->root->getElement();

        // If the size is 1 the heap will be empty
        if (this->size() == 1)
        {
            delete this->root;
            this->root = nullptr;
            lastNode = nullptr;
        }
        else
        {
            // Get the new last node
            HeapNode<T>* newLast = getNewLastNode();

            // Check which child the old last node is & set to null
            if (lastNode->getParent()->getLeft() == lastNode)
                lastNode->getParent()->setLeft(nullptr);
            else
                lastNode->getParent()->setRight(nullptr);

            static_cast<HeapNode<T>*>(this->root)->setElement(lastNode->getElement());
            delete lastNode;
            lastNode = newLast;
            heapifyRemove();
        }
        this->modCount++;
        return minElement;
    }

    // Reorders this heap after removing the root element.
    void heapifyRemove()
    {
        T temp;
        HeapNode<T>* node = static_cast<HeapNode<T>*>(this->root);
        HeapNode<T>* left = static_cast<HeapNode<T>*>(node->getLeft());
        HeapNode<T>* right = static_cast<HeapNode<T>*>(node->getRight());
        HeapNode<T>* next;

        if ((left == nullptr) && (right == nullptr))
            // no children
            next = nullptr;
        else if (right == nullptr)
            // one child
            next = left;
        else if (left->getElement() < right->getElement())
            // two children, left is smaller
            next = left;
        else
            // two children, right is smaller
            next = right;

        temp = node->getElement();
        while ((next != nullptr) && (next->getElement() < temp))
        {
            node->setElement(next->getElement());
            node = next;
            left = static_cast<HeapNode<T>*>(node->getLeft());
            right = static_cast<HeapNode<T>*>(node->getRight());

            if ((left == nullptr) && (right == nullptr))
                next = nullptr;
            else if (right == nullptr)
                next = left;
            else if (left->getElement() < right->getElement())
                next = left;
            else
                next = right;
        }
        node->setElement(temp);
    }

    // Returns the node that will be the new last node after a remove.
    HeapNode<T>* getNewLastNode()
    {
        HeapNode<T>* newLastNode = lastNode;

        while ((newLastNode != this->root) && (newLastNode->getParent()->getLeft() == newLastNode))
            newLastNode = newLastNode->getParent();

        if (newLastNode != this->root)
            newLastNode = static_cast<HeapNode<T>*>(newLastNode->getParent()->getLeft());

        while (newLastNode->getRight() != nullptr)
            newLastNode = static_cast<HeapNode<T>*>(newLastNode->getRight());

        return newLastNode;
    }

    // Returns the element with the lowest value in this heap.
    T findMin()
    {
        if (this->isEmpty())
            throw EmptyCollectionException("LinkedHeap");

        return this->root->getElement();
    }
};

#endif
