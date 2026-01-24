package heaps.linkedheap;

import java.util.*;

import heaps.linkedheap.exceptions.*;

/**
 * LinkedBinaryTree implements the BinaryTreeADT interface.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class LinkedBinaryTree<T> implements Iterable<T>
{
	protected BinaryTreeNode<T> root; 
	protected int modCount;

	/**
	 * Creates an empty binary tree.
	 */
	public LinkedBinaryTree() 
	{
		root = null;
	}

	/**
	 * Creates a binary tree with the specified element as its root.
	 *
	 * @param element the element that will become the root of the binary tree
	 */
	public LinkedBinaryTree(T element) 
	{
		root = new BinaryTreeNode<T>(element);
	}

	/**
	 * Creates a binary tree with the specified element as its root and the 
	 * given trees as its left child and right child
	 *
	 * @param element the element that will become the root of the binary tree
	 * @param left the left subtree of this tree
	 * @param right the right subtree of this tree
	 */
	public LinkedBinaryTree(T element, LinkedBinaryTree<T> left, 
			LinkedBinaryTree<T> right) 
	{
		root = new BinaryTreeNode<T>(element);
		root.setLeft(left.root);
		root.setRight(right.root);
	}

	/**
	 * Returns a reference to the element at the root
	 *
	 * @return a reference to the specified target
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T getRootElement() throws EmptyCollectionException
	{
        if (root == null)
            throw new EmptyCollectionException("LinkedBinaryTree");
        
        return (root.getElement());
	}

	/**
	 * Returns a reference to the node at the root
	 *
	 * @return a reference to the specified node
	 * @throws EmptyCollectionException if the tree is empty
	 */
	protected BinaryTreeNode<T> getRootNode() throws EmptyCollectionException
	{
        if (root == null)
            throw new EmptyCollectionException("LinkedBinaryTree");
        
        return (root);
	}

	/**
	 * Returns the left subtree of the root of this tree.
	 *
	 * @return a link to the left subtree of the tree
	 */
	public LinkedBinaryTree<T> getLeft()
	{
		if (root == null)
			throw new EmptyCollectionException("LinkedBinaryTree - getLeft() -");

        LinkedBinaryTree<T> result = new LinkedBinaryTree<T>();
        result.root = root.getLeft();
        
        return result;
	}

	/**
	 * Returns the right subtree of the root of this tree.
	 *
	 * @return a link to the right subtree of the tree
	 */
	public LinkedBinaryTree<T> getRight()
	{
		if (root == null)
			throw new EmptyCollectionException("LinkedBinaryTree - getRight() -");

		LinkedBinaryTree<T> result = new LinkedBinaryTree<T>();
		result.root = root.getRight();

		return result;
	}

	/**
	 * Returns true if this binary tree is empty and false otherwise.
	 *
	 * @return true if this binary tree is empty, false otherwise
	 */
	public boolean isEmpty() 
	{
		return (root == null);
	}

	/**
	 * Returns the integer size of this tree.
	 *
	 * @return the integer size of the tree
	 */
	public int size() 
	{
		if (root == null) {
			return 0;
		}

        return root.numChildren() + 1;
	}

	/**
	 * Returns the height of this tree.
	 *
	 * @return the height of the tree
	 */
	public int getHeight()
	{
        return height(root) - 1;
	}

	/**
	 * Returns the height of the specified node.
	 *
	 * @param node the node from which to calculate the height
	 * @return the height of the tree
	 */
	private int height(BinaryTreeNode<T> node) 
	{
        int result = 0;
        if (node != null)
            result = Math.max(height(node.getLeft()), height(node.getRight())) + 1;

        return result;
	}

	/**
	 * Returns true if this tree contains an element that matches the
	 * specified target element and false otherwise.
	 *
	 * @param targetElement the element being sought in this tree
	 * @return true if the element in is this tree, false otherwise
	 */
	public boolean contains(T targetElement) 
	{
        T temp;
        boolean found = false;
        
        try 
        {
            temp = find(targetElement);
            found = true;
        }
        catch (Exception ElementNotFoundException) 
        {
            found = false;
        }
        
        return found;
	}

	/**
	 * Returns a reference to the specified target element if it is
	 * found in this binary tree.  Throws a ElementNotFoundException if
	 * the specified target element is not found in the binary tree.
	 *
	 * @param targetElement the element being sought in this tree
	 * @return a reference to the specified target
	 * @throws ElementNotFoundException if the element is not in the tree
	 */
	public T find(T targetElement) throws ElementNotFoundException
	{
		BinaryTreeNode<T> current = findNode(targetElement, root);

		if (current == null)
			throw new ElementNotFoundException("LinkedBinaryTree");

		return (current.getElement());
	}

	/**
	 * Returns a reference to the specified target element if it is
	 * found in this binary tree.
	 *
	 * @param targetElement the element being sought in this tree
	 * @param next the element to begin searching from
	 */
	private BinaryTreeNode<T> findNode(T targetElement, 
			BinaryTreeNode<T> next)
	{
		if (next == null)
			return null;

		if (next.getElement().equals(targetElement))
			return next;

		BinaryTreeNode<T> temp = findNode(targetElement, next.getLeft());

		if (temp == null)
			temp = findNode(targetElement, next.getRight());

		return temp;
	}

	/**
	 * Returns a string representation of this binary tree showing
	 * the nodes in an inorder fashion.
	 *
	 * @return a string representation of this binary tree
	 */
	public String toString() 
	{
        ArrayList<T> tempList = new ArrayList<T>();
        inOrder(root, tempList);
      
        String ret = "";
        
        for (T element : tempList) {
        	ret += element.toString() + " ";
        }
        
        return ret;
	}

	/**
	 * Returns an iterator over the elements in this tree using the 
	 * iteratorInOrder method
	 *
	 * @return an in order iterator over this binary tree
	 */
	public Iterator<T> iterator()
	{
		return iteratorInOrder();
	}

	/**
	 * Performs an inorder traversal on this binary tree by calling an
	 * overloaded, recursive inorder method that starts with
	 * the root.
	 *
	 * @return an in order iterator over this binary tree
	 */
	public Iterator<T> iteratorInOrder()
	{
		ArrayList<T> tempList = new ArrayList<T>();
		inOrder(root, tempList);

		return new TreeIterator(tempList.iterator());
	}

	/**
	 * Performs a recursive inorder traversal.
	 *
	 * @param node the node to be used as the root for this traversal
	 * @param tempList the temporary list for use in this traversal
	 */
	protected void inOrder(BinaryTreeNode<T> node, 
			ArrayList<T> tempList) 
	{
		if (node != null)
		{
			inOrder(node.getLeft(), tempList);
			tempList.add(node.getElement());
			inOrder(node.getRight(), tempList);
		}
	}

	/**
	 * Inner class to represent an iterator over the elements of this tree
	 */
	private class TreeIterator implements Iterator<T>
	{
		private int expectedModCount;
		private Iterator<T> iter;

		/**
		 * Sets up this iterator using the specified iterator.
		 *
		 * @param iter the list iterator created by a tree traversal
		 */
		public TreeIterator(Iterator<T> iter)
		{
			this.iter = iter;
			expectedModCount = modCount;
		}

		/**
		 * Returns true if this iterator has at least one more element
		 * to deliver in the iteration.
		 *
		 * @return  true if this iterator has at least one more element to deliver
		 *          in the iteration
		 * @throws  ConcurrentModificationException if the collection has changed
		 *          while the iterator is in use
		 */
		public boolean hasNext() throws ConcurrentModificationException
		{
			if (!(modCount == expectedModCount))
				throw new ConcurrentModificationException();

			return (iter.hasNext());
		}

		/**
		 * Returns the next element in the iteration. If there are no
		 * more elements in this iteration, a NoSuchElementException is
		 * thrown.
		 *
		 * @return the next element in the iteration
		 * @throws NoSuchElementException if the iterator is empty
		 */
		public T next() throws NoSuchElementException
		{
			if (hasNext())
				return (iter.next());
			else 
				throw new NoSuchElementException();
		}

		/**
		 * The remove operation is not supported.
		 * 
		 * @throws UnsupportedOperationException if the remove operation is called
		 */
		public void remove()
		{
			throw new UnsupportedOperationException();
		}
	}
}

