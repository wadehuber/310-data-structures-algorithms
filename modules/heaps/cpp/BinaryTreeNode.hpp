// BinaryTreeNode represents a node in a binary tree with a left and
// right child.
//
// 1-1 conversion of heaps/linkedheap/BinaryTreeNode.java
#ifndef BINARY_TREE_NODE_HPP
#define BINARY_TREE_NODE_HPP

#include <cstddef>

template <typename T>
class BinaryTreeNode
{
protected:
    T element;
    BinaryTreeNode<T>* left;
    BinaryTreeNode<T>* right;

public:
    // Creates a new tree node with the specified data.
    BinaryTreeNode(T obj)
    {
        element = obj;
        left = nullptr;
        right = nullptr;
    }

    virtual ~BinaryTreeNode() {}

    // Returns the number of non-null children of this node.
    int numChildren()
    {
        int children = 0;

        if (left != nullptr)
            children = 1 + left->numChildren();

        if (right != nullptr)
            children = children + 1 + right->numChildren();

        return children;
    }

    // Return the element at this node.
    T getElement() { return element; }

    // Return the right child of this node.
    BinaryTreeNode<T>* getRight() { return right; }

    // Sets the right child of this node.
    void setRight(BinaryTreeNode<T>* node) { right = node; }

    // Return the left child of this node.
    BinaryTreeNode<T>* getLeft() { return left; }

    // Sets the left child of this node.
    void setLeft(BinaryTreeNode<T>* node) { left = node; }
};

#endif
