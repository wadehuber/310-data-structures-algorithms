package binarytreereview;

import binarytreereview.exceptions.*;

/**
 * LinkedBinarySearchTree implements the BinarySearchTreeADT interface 
 * with links.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class LinkedBinarySearchTree<T> extends LinkedBinaryTree<T> 
{
	/**
	 * Creates an empty binary search tree.
	 */
	public LinkedBinarySearchTree() 
	{
		super();
	}

	/**
	 * Creates a binary search with the specified element as its root.
	 *
	 * @param element the element that will be the root of the new binary
	 *        search tree
	 */
	public LinkedBinarySearchTree(T element) 
	{
		super(element);

		if (!(element instanceof Comparable))
			throw new NonComparableElementException("LinkedBinarySearchTree");
	}

	/**
	 * Adds the specified object to the binary search tree in the
	 * appropriate position according to its natural order.  Note that
	 * equal elements are added to the right.
	 *
	 * @param element the element to be added to the binary search tree
	 */
	public void addElement(T element) 
	{
		if (!(element instanceof Comparable))
			throw new NonComparableElementException("LinkedBinarySearchTree");

		if (isEmpty())
			root = new BinaryTreeNode<T>(element);
		else
			addElement(element, root);
		modCount++;
	}

	/**
	 * Adds the specified object to the binary search tree in the
	 * appropriate position according to its natural order.  Note that
	 * equal elements are added to the right.
	 *
	 * @param element the element to be added to the binary search tree
	 */
	private void addElement(T element, BinaryTreeNode<T> root) 
	{
		Comparable<T> comparableElement = (Comparable<T>) element;

		if (comparableElement.compareTo(root.getElement()) < 0)
		{
			if (root.getLeft() == null) 
				root.setLeft(new BinaryTreeNode<T>(element));
			else
				addElement(element, root.getLeft());
		}
		else
		{
			if (root.getRight() == null) 
				root.setRight(new BinaryTreeNode<T>(element));
			else
				addElement(element, root.getRight());
		}
	}

	/**
	 * Removes the first element that matches the specified target
	 * element from the binary search tree and returns a reference to
	 * it.  Throws a ElementNotFoundException if the specified target
	 * element is not found in the binary search tree.
	 *
	 * @param targetElement the element being sought in the binary search tree
	 * @throws ElementNotFoundException if the target element is not found
	 */
	public T removeElement(T targetElement)
			throws ElementNotFoundException 
	{
		T result = null;

		if (isEmpty())
			throw new ElementNotFoundException("LinkedBinarySearchTree");
		else
		{
			BinaryTreeNode<T> parent = null;
			if (((Comparable<T>)targetElement).equals(root.element)) 
			{ // Remove the root
				result = root.element;
				BinaryTreeNode<T> inOrderSuccessor = replacement(root);
				if (inOrderSuccessor == null)
					root = null;
				else 
				{
					root.element = inOrderSuccessor.element;
					root.setRight(inOrderSuccessor.right);
					root.setLeft(inOrderSuccessor.left);
				}

				modCount++;
			}
			else 
			{ // Look for the target in a sub-tree               
				parent = root;
				if (((Comparable<T>)targetElement).compareTo(root.element) < 0)
					result = removeElement(targetElement, root.getLeft(), parent);
				else
					result = removeElement(targetElement, root.getRight(), parent);
			}
		}

		return result;
	}

	/**
	 * Removes the first element that matches the specified target
	 * element from the binary search tree and returns a reference to
	 * it.  Throws a ElementNotFoundException if the specified target
	 * element is not found in the binary search tree.
	 *
	 * @param targetElement the element being sought in the binary search tree
	 * @param node the node from which to search
	 * @param parent the parent of the node from which to search
	 * @throws ElementNotFoundException if the target element is not found
	 */
	private T removeElement(T targetElement, BinaryTreeNode<T> node, BinaryTreeNode<T> parent)
			throws ElementNotFoundException 
	{
		T result = null;

		if (node == null)
			throw new ElementNotFoundException("LinkedBinarySearchTree");
		else
		{
			if (((Comparable<T>)targetElement).equals(node.element)) 
			{   // remove the current node
				result =  node.element;
				BinaryTreeNode<T> inOrderSuccessor = replacement(node);
				// Decide if current node is left or right child of the parent
				if (parent.right == node)
					parent.right = inOrderSuccessor;
				else 
					parent.left = inOrderSuccessor;

				modCount++;
			}
			else 
			{   // Look for the target in a sub-tree            
				parent = node;
				if (((Comparable<T>)targetElement).compareTo(node.element) < 0)
					result = removeElement(targetElement, node.getLeft(), parent);
				else
					result = removeElement(targetElement, node.getRight(), parent);
			}
		}

		return result;
	}

	/**
	 * Returns a reference to a node that will replace the one
	 * specified for removal. In the case where the removed node has 
	 * two children, the inorder successor is used as its replacement.
	 *
	 * @param root the node to be removed
	 * @return a reference to the replacing node
	 */
	private BinaryTreeNode<T> replacement(BinaryTreeNode<T> root) 
	{
		BinaryTreeNode<T> result = null;

		// No children
		if ((root.left == null) && (root.right == null))
			result = null;

		// One child - left
		else if ((root.left != null) && (root.right == null))
			result = root.left;

		// One child - right
		else if ((root.left == null) && (root.right != null))
			result = root.right;

		// Two children
		else
		{
			BinaryTreeNode<T> current = root.right;
			BinaryTreeNode<T> parent = root;

			// Go all the way to the left in the right sub-tree
			while (current.left != null)
			{
				parent = current;
				current = current.left;
			}

			// Set the replacement's left subtree to the root's left subtree
			current.left = root.left;
			
			// If the right child of the root is not the left-most node in
			//  the right sub tree
			if (root.right != current)
			{
				parent.left = current.right;
				current.right = root.right;
			}

			result = current;
		}

		return result;
	}

	/**
	 * Removes elements that match the specified target element from 
	 * the binary search tree. Throws a ElementNotFoundException if 
	 * the specified target element is not found in this tree.
	 *
	 * @param targetElement the element being sought in the binary search tree
	 * @throws ElementNotFoundException if the target element is not found
	 */
	public void removeAllOccurrences(T targetElement)
			throws ElementNotFoundException 
	{
		removeElement(targetElement);

		try
		{
			while (true) {
				
				removeElement(targetElement);
			}
		}
		catch (Exception ElementNotFoundException)
		{
		}
	}

	/**
	 * Removes the node with the least value from the binary search
	 * tree and returns a reference to its element. Throws an
	 * EmptyCollectionException if this tree is empty. 
	 *
	 * @return a reference to the node with the least value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T removeMin() throws EmptyCollectionException 
	{
		T result = null;

		if (isEmpty())
			throw new EmptyCollectionException("LinkedBinarySearchTree");
		else 
		{
			if (root.left == null) 
			{  // Root is the min element
				result = root.element;
				root = root.right;
			}
			else 
			{  // Min element is all the way to the left
				BinaryTreeNode<T> parent = root;
				BinaryTreeNode<T> current = root.left;
				while (current.left != null) 
				{
					parent = current;
					current = current.left;
				}
				result =  current.element;
				parent.left = current.right;
			}

			modCount++;
		}

		return result;
	}

	/**
	 * Removes the node with the highest value from the binary
	 * search tree and returns a reference to its element. Throws an
	 * EmptyCollectionException if this tree is empty. 
	 *
	 * @return a reference to the node with the highest value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T removeMax() throws EmptyCollectionException 
	{
		// To be completed as a Programming Project
		
		return null;  // temp
	}

	/**
	 * Returns the element with the least value in the binary search
	 * tree. It does not remove the node from the binary search tree. 
	 * Throws an EmptyCollectionException if this tree is empty.
	 *
	 * @return the element with the least value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T findMin() throws EmptyCollectionException 
	{
		// To be completed as a Programming Project
		
		return null;  // temp
	}
	
	/**
	 * Returns the element that matches targetElement in the binary search
	 * tree. It does not remove the node from the binary search tree. 
	 * Throws an EmptyCollectionException if this tree is empty.
	 *
	 * @return the that matches targetElement
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T find(T targetElement) throws EmptyCollectionException 
	{
		// To be completed as a Programming Project
		//  Do not call super.find()!
		
		return null;  // temp
	}

	/**
	 * Returns the element with the highest value in the binary
	 * search tree. It does not remove the node from the binary
	 * search tree. Throws an EmptyCollectionException if this 
	 * tree is empty.
	 *
	 * @return the element with the highest value
	 * @throws EmptyCollectionException if the tree is empty
	 */
	public T findMax() throws EmptyCollectionException 
	{
		// To be completed as a Programming Project
		
		return null;  // temp
	}

	/**
	 * Returns the left subtree of the root of this tree.
	 *
	 * @return a link to the left subtree of the tree
	 */
	public LinkedBinarySearchTree<T> getLeft()
	{
		// To be completed as a Programming Project
		
		return null;  // temp
	}

	/**
	 * Returns the right subtree of the root of this tree.
	 *
	 * @return a link to the right subtree of the tree
	 */
	public LinkedBinarySearchTree<T> getRight()
	{
		// To be completed as a Programming Project
		
		return null;  // temp
	}
}

