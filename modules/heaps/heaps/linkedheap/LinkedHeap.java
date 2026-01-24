package heaps.linkedheap;

import heaps.linkedheap.exceptions.*;

/**
 * LinkedHeap implements a heap.
 *
 * @author Java Foundations
 * @version 4.0
 */
public class LinkedHeap<T> extends LinkedBinaryTree<T> implements HeapADT<T> 
{
	public HeapNode<T> lastNode;  

	public LinkedHeap() 
	{
		super();
	}

	/**
	 * Adds the specified element to this heap in the appropriate
	 * position according to its key value. 
	 *
	 * @param obj the element to be added to the heap
	 */
	public void addElement(T obj) 
	{
		HeapNode<T> node = new HeapNode<T>(obj);

		if (root == null)
			root=node;
		else
		{
			HeapNode<T> nextParent = getNextParentAdd(); // keep heap structure
			// Determine which child
			if (nextParent.getLeft() == null)  // no children
				nextParent.setLeft(node);
			else                               // one child - the left node
				nextParent.setRight(node);

			node.setParent(nextParent);
		}
		lastNode = node;
		modCount++;

		if (size() > 1)
			heapifyAdd();  // keep the heap ordering
	}

	/**
	 * Returns the node that will be the parent of the new node
	 *
	 * @return the node that will be the parent of the new node
	 */
	private HeapNode<T> getNextParentAdd()
	{
		HeapNode<T> result = lastNode;

		// Get to the left sub-tree or the root
		while ((result != root) && (result.getParent().getLeft() != result))
			result = result.getParent();
		
		if (result != root)
			// Go to the parent's right subtree
			if (result.getParent().getRight() == null)
				// Parent has no right child, so parent is the new parent
				result = result.getParent();
			else
			{
				// Get parent's right child
				result = (HeapNode<T>)result.getParent().getRight();
				// Go all the way to the left
				while (result.getLeft() != null)
					result = (HeapNode<T>)result.getLeft();
			}
		else
			// Tree is full so go all the way to the left (start a new row of leaves)
			while (result.getLeft() != null)
				result = (HeapNode<T>)result.getLeft();

		return result;
	}

	/**
	 * Reorders this heap after adding a node.
	 */
	private void heapifyAdd()
	{
		T temp;
		HeapNode<T> next = lastNode;

		temp = next.getElement();

		while ((next != root) && 
				(((Comparable<T>)temp).compareTo(next.getParent().getElement()) < 0))
		{
			next.setElement(next.getParent().getElement());
			next = next.parent;
		}
		next.setElement(temp);
	}

	/**
	 * Remove the element with the lowest value in this heap and
	 * returns a reference to it. Throws an EmptyCollectionException 
	 * if the heap is empty.
	 *
	 * @return the element with the lowest value in this heap
	 * @throws EmptyCollectionException if the heap is empty
	 */
	public T removeMin() throws EmptyCollectionException 
	{
		if (isEmpty())
			throw new EmptyCollectionException("LinkedHeap");

		T minElement =  root.getElement();

		// If the size is 1 the heap will be empty
		if (size() == 1)
		{
			root = null;
			lastNode = null;
		}
		else
		{
			// Get the new last node
			HeapNode<T> newLast = getNewLastNode();
			
			// Check which child the old last node is & set to null
			if (lastNode.getParent().getLeft() == lastNode)
				lastNode.getParent().setLeft(null);
			else
				lastNode.getParent().setRight(null);

			((HeapNode<T>)root).setElement(lastNode.getElement());
			lastNode = newLast;
			heapifyRemove();
		}
		modCount++;
		return minElement;
	}

	/**
	 * Reorders this heap after removing the root element.
	 */
	private void heapifyRemove()
	{
		T temp;
		HeapNode<T> node = (HeapNode<T>)root;
		HeapNode<T> left = (HeapNode<T>)node.getLeft();
		HeapNode<T> right = (HeapNode<T>)node.getRight();
		HeapNode<T> next;

		
		if ((left == null) && (right == null))
			// no children
			next = null;
		else if (right == null)
			// one child
			next = left;
		else if (((Comparable<T>)left.getElement()).compareTo(right.getElement()) < 0)
			// two children, left is smaller
			next = left;
		else
			// two children, right is smaller
			next = right;

		temp = node.getElement();
		while ((next != null) && 
				(((Comparable<T>)next.getElement()).compareTo(temp) < 0))
		{
			node.setElement(next.getElement());
			node = next;
			left = (HeapNode<T>)node.getLeft();
			right = (HeapNode<T>)node.getRight();

			if ((left == null) && (right == null))
				next = null;
			else if (right == null)
				next = left;
			else if (((Comparable<T>)left.getElement()).compareTo(right.getElement()) < 0)
				next = left;
			else
				next = right;
		}
		node.setElement(temp);
	}

	/**
	 * Returns the node that will be the new last node after a remove.
	 *
	 * @return the node that will be the new last node after a remove
	 */
	private HeapNode<T> getNewLastNode()
	{
		HeapNode<T> newLastNode = lastNode;

		
		while ((newLastNode != root) && (newLastNode.getParent().getLeft() == newLastNode))
			newLastNode = newLastNode.getParent();

		if (newLastNode != root)
			newLastNode = (HeapNode<T>)newLastNode.getParent().getLeft();

		while (newLastNode.getRight() != null)
			newLastNode = (HeapNode<T>)newLastNode.getRight();

		return newLastNode;
	}

	/**
	 * Returns the element with the lowest value in this heap.
	 * Throws an EmptyCollectionException if the heap is empty.
	 *
	 * @return the element with the lowest value in this heap
	 * @throws EmptyCollectionException if the heap is empty
	 */
	public T findMin() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("LinkedHeap");

		return root.getElement();
	}
	
}









