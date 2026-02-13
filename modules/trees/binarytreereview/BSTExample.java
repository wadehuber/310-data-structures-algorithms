package binarytreereview;

import java.util.ArrayList;
import java.util.Iterator;

public class BSTExample {

	public static void main(String[] args) {
		LinkedBinarySearchTree<Integer> t = new LinkedBinarySearchTree<Integer>();
		
		for (int ii=0;ii<20;ii++) {
			t.addElement((int) (Math.random()* 100));
		}

		// add 4 extra 10s to test removeAllOccurrences 
		t.addElement(10);
		t.addElement(10);
		t.addElement(10);
		t.addElement(10);
		
		System.out.println("Tree: " + t);
		
		System.out.println("Find 5: " + t.find(5));
		
		System.out.println();
		System.out.print("Traversals:");
		System.out.print("  Pre-Order:");
		Iterator<Integer> preorder = t.iteratorPreOrder();
		while (preorder.hasNext()) {
			System.out.print(preorder.next() + " ");
		}
		System.out.println();

		System.out.print("  In-Order:");
		Iterator<Integer> inorder = t.iteratorInOrder();
		while (inorder.hasNext()) {
			System.out.print(inorder.next() + " ");
		}
		System.out.println();

		System.out.print("  Post-Order:");
		Iterator<Integer> postorder = t.iteratorPostOrder();
		while (postorder.hasNext()) {
			System.out.print(postorder.next() + " ");
		}
		System.out.println();

		System.out.print("  Level-Order:");
		Iterator<Integer> levelorder = t.iteratorLevelOrder();
		while (levelorder.hasNext()) {
			System.out.print(levelorder.next() + " ");
		}
		System.out.println();

		System.out.println();
		System.out.println("Test removeAllOccurrences (10):");
		System.out.println("Before: " + t);
		t.removeAllOccurrences(10);
		System.out.println(" After: " + t);
		
	}

}
