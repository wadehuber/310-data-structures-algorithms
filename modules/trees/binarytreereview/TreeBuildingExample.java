package binarytreereview;
import java.util.Iterator;

public class TreeBuildingExample {

	public static void main(String[] args) {
		
		// We will build the following tree:
		//      A
		//    /   \
		//   B     E
		//  / \   /
		// C   D F
		
		////////////////////////////////////////////////////////////////////////
		// Bottom up - create the leaves, then the parents
		// Level 2 - Leaves
		LinkedBinaryTree<String> c = new LinkedBinaryTree<String>("C");
		LinkedBinaryTree<String> d = new LinkedBinaryTree<String>("D");
		LinkedBinaryTree<String> f = new LinkedBinaryTree<String>("F");
		
		// Level 1 - Interior nodes
		LinkedBinaryTree<String> b = new LinkedBinaryTree<String>("B",c,d);
		LinkedBinaryTree<String> e = new LinkedBinaryTree<String>("E",f,null);
		
		// Root
		LinkedBinaryTree<String> a1 = new LinkedBinaryTree<String>("A",b,e);


		System.out.println("toString(): " + a1);
		System.out.println("getHeight() = " + a1.getHeight());
		System.out.println("size() = " + a1.size());
		System.out.println("getLeft() of A: " + a1.getLeft().getRootElement());
		System.out.println("getRight() of A: " + a1.getRight().getRootElement());
		if ( (a1.contains("A")) && (a1.contains("B")) && (a1.contains("D")) && 
				(a1.contains("E")) && (a1.contains("Z") == false)) {
			System.out.println("contains() works!");
		}
		else
			System.out.println("contains() does not work!");
		System.out.println("Found " + a1.find("A"));
		System.out.println("Found " + a1.find("B"));
		System.out.println("Found " + a1.find("C"));
		System.out.println("Found " + a1.find("D"));
		System.out.println("Found " + a1.find("E"));
		System.out.println("Found " + a1.find("F"));
		// System.out.println("Found " + a1.find("X"));
		System.out.println();

		
		System.out.print ("Pre-order traversal: ");
		Iterator<String> pre = a1.iteratorPreOrder();
		while (pre.hasNext()) {
			System.out.print (pre.next());
		}
		System.out.println();

		System.out.print ("In-order traversal: ");
		Iterator<String> in = a1.iteratorInOrder();
		while (in.hasNext()) {
			System.out.print (in.next());
		}
		System.out.println();

		System.out.print ("Post-order traversal: ");
		Iterator<String> post = a1.iteratorPostOrder();
		while (post.hasNext()) {
			System.out.print (post.next());
		}
		System.out.println();
		
		System.out.print ("Level-order traversal: ");
		Iterator<String> level = a1.iteratorLevelOrder();
		while (level.hasNext()) {
			System.out.print (level.next());
		}
		System.out.println();
	
		////////////////////////////////////////////////////////////////////////
		// In one line using the nodes created for the bottom up method
  		LinkedBinaryTree<String> a3 = 
	  			new LinkedBinaryTree<String>(
	  				"A",
	  				new LinkedBinaryTree<String>(
	  						"B",
	  						new LinkedBinaryTree<String>("C"),
	  						new LinkedBinaryTree<String>("D")),
	  				new LinkedBinaryTree<String>(
	  						"E",
	  						new LinkedBinaryTree<String>("F")
	 						,null));
  		
		System.out.println("\n\nOne liner: " + a3);
	}

}
