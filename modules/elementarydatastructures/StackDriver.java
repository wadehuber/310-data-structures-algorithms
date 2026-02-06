package videoexamples.stacksqueues.csc205;

public class StackDriver {

	public static void main(String args[]) {
		System.out.println("FastStack testing:");
	
		FastStack<String> stack1 = new FastStack<String>();
		FastStack<Integer> stack2 = new FastStack<Integer>();
	
		stack1.push("neworleans");
		stack1.push("tampabay");
		stack1.push("carolina");
		stack1.push("atlanta");
		
		for(int x=1;x<10;x++) {
			stack2.push(x);
		}
		System.out.println("Stack1 (size=" + stack1.size() + "): " + stack1);
		System.out.println("Stack2 (size=" + stack2.size() + "): " + stack2);
		
		stack1.pop();
		stack2.pop();
		stack2.pop();
		stack2.pop();
		
		System.out.println("After pop():");
		System.out.println("Stack1 (size=" + stack1.size() + "): " + stack1);
		System.out.println("Stack2 (size=" + stack2.size() + "): " + stack2);
	}

}
