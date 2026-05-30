// LinkedBinaryTree implements a binary tree.
//
// 1-1 conversion of heaps/linkedheap/LinkedBinaryTree.java
// (the in-order toString is kept; the iterator's concurrent-modification
// machinery is left out as it is Java-specific boilerplate).
#ifndef LINKED_BINARY_TREE_HPP
#define LINKED_BINARY_TREE_HPP

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

#include "BinaryTreeNode.hpp"
#include "Exceptions.hpp"

// Helper that turns an element into a string via operator<< (the C++
// equivalent of Java's element.toString()).
template <typename T>
std::string toDisplayString(const T& element)
{
    std::ostringstream oss;
    oss << element;
    return oss.str();
}

template <typename T>
class LinkedBinaryTree
{
protected:
    BinaryTreeNode<T>* root;
    int modCount;

public:
    // Creates an empty binary tree.
    LinkedBinaryTree()
    {
        root = nullptr;
        modCount = 0;
    }

    // Creates a binary tree with the specified element as its root.
    LinkedBinaryTree(T element)
    {
        root = new BinaryTreeNode<T>(element);
        modCount = 0;
    }

    virtual ~LinkedBinaryTree() {}

    // Returns a reference to the element at the root.
    T getRootElement()
    {
        if (root == nullptr)
            throw EmptyCollectionException("LinkedBinaryTree");

        return root->getElement();
    }

    // Returns a reference to the node at the root.
    BinaryTreeNode<T>* getRootNode()
    {
        if (root == nullptr)
            throw EmptyCollectionException("LinkedBinaryTree");

        return root;
    }

    // Returns the left subtree of the root of this tree.
    LinkedBinaryTree<T> getLeft()
    {
        if (root == nullptr)
            throw EmptyCollectionException("LinkedBinaryTree - getLeft() -");

        LinkedBinaryTree<T> result;
        result.root = root->getLeft();

        return result;
    }

    // Returns the right subtree of the root of this tree.
    LinkedBinaryTree<T> getRight()
    {
        if (root == nullptr)
            throw EmptyCollectionException("LinkedBinaryTree - getRight() -");

        LinkedBinaryTree<T> result;
        result.root = root->getRight();

        return result;
    }

    // Returns true if this binary tree is empty and false otherwise.
    bool isEmpty() { return (root == nullptr); }

    // Returns the integer size of this tree.
    int size()
    {
        if (root == nullptr)
            return 0;

        return root->numChildren() + 1;
    }

    // Returns the height of this tree.
    int getHeight() { return height(root) - 1; }

    // Returns the height of the specified node.
    int height(BinaryTreeNode<T>* node)
    {
        int result = 0;
        if (node != nullptr)
            result = std::max(height(node->getLeft()), height(node->getRight())) + 1;

        return result;
    }

    // Returns true if this tree contains a matching element.
    bool contains(T targetElement)
    {
        bool found = false;

        try
        {
            find(targetElement);
            found = true;
        }
        catch (const ElementNotFoundException&)
        {
            found = false;
        }

        return found;
    }

    // Returns the specified target element if it is found in this tree.
    T find(T targetElement)
    {
        BinaryTreeNode<T>* current = findNode(targetElement, root);

        if (current == nullptr)
            throw ElementNotFoundException("LinkedBinaryTree");

        return current->getElement();
    }

    // Returns the node holding the target element, or null.
    BinaryTreeNode<T>* findNode(T targetElement, BinaryTreeNode<T>* next)
    {
        if (next == nullptr)
            return nullptr;

        if (next->getElement() == targetElement)
            return next;

        BinaryTreeNode<T>* temp = findNode(targetElement, next->getLeft());

        if (temp == nullptr)
            temp = findNode(targetElement, next->getRight());

        return temp;
    }

    // Returns an in-order string representation of this binary tree.
    std::string toString()
    {
        std::vector<T> tempList;
        inOrder(root, tempList);

        std::string ret = "";

        for (const T& element : tempList)
            ret += toDisplayString(element) + " ";

        return ret;
    }

    // Performs a recursive in-order traversal.
    void inOrder(BinaryTreeNode<T>* node, std::vector<T>& tempList)
    {
        if (node != nullptr)
        {
            inOrder(node->getLeft(), tempList);
            tempList.push_back(node->getElement());
            inOrder(node->getRight(), tempList);
        }
    }
};

#endif
