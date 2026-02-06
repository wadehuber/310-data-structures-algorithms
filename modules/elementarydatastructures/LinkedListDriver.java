package videoexamples.lists;

import videoexamples.lists.csc205.LinkedList;

public class LinkedListDriver {

	public static void main(String[] args) {
		LinkedList<String> myList = new LinkedList<String>();
		String[] searchValues = {"Hello", "World", "Arizona", "CGCC", "Chandler", "205"};
		
		myList.addToFront("World");
		myList.addToFront("Hello");
		myList.addToRear("Chandler");
		myList.addToRear("Gilbert");
		
		System.out.println(myList);
		
		System.out.println("Size = " + myList.size());
		System.out.println("First = " + myList.first());
		System.out.println("Last = " + myList.last());
		
		if (myList.isEmpty()) {
			System.out.println("List is empty");
		}
		else {
			System.out.println("List is not empty");
		}

		System.out.println();
		System.out.println("Iterator test:");
		System.out.print("  ");
		for(String s : myList) {
			System.out.print(s + " ");
		}
		System.out.println();
		
		System.out.println();
		System.out.println("Contains testing (part 1):");
		for (String val : searchValues) {
			if (myList.contains(val)) {
				System.out.println("  myList contains " + val + " at index " + myList.indexOf(val));
			}
			else {
				System.out.println("  myList does not contain " + val + " index=" + myList.indexOf(val));
			}
		}
		
		System.out.println();
		System.out.println("Remove some stuff:");
		String front = myList.removeFirst();
		String rear = myList.removeLast();
		System.out.println("Old front = " + front);
		System.out.println("Old rear = " + rear);
		System.out.println("Current list = " + myList);
		System.out.println("Size = " + myList.size());
		System.out.println("First = " + myList.first());
		System.out.println("Last = " + myList.last());

		System.out.println();
		System.out.println("Contains testing (part 2):");
		for (String val : searchValues) {
			if (myList.contains(val)) {
				System.out.println("  myList contains " + val + " at index " + myList.indexOf(val));
			}
			else {
				System.out.println("  myList does not contain " + val + " index=" + myList.indexOf(val));
			}
		}


		System.out.println();
		System.out.println("Remove the rest of the nodes:");
		front = myList.removeFirst();
		rear = myList.removeLast();
		System.out.println("Old front = " + front);
		System.out.println("Old rear = " + rear);
		System.out.println("Current list = " + myList);
		System.out.println("Size = " + myList.size());
		
		System.out.println();
		System.out.println("Finishing up:");
		myList.addToFront("The");
		myList.addToRear("End");
		System.out.println("First = " + myList.first());
		System.out.println("Last = " + myList.last());
		System.out.println("Current list = " + myList);
		System.out.println("Size = " + myList.size());
	}
}
