package videoexamples.stacksqueues.csc205;

public class QueueDriver {

	public static void main(String[] args) {
		System.out.println("FastQueue testing:");
		
		FastQueue<String> queue1 = new FastQueue<String>();
		FastQueue<Integer> queue2 = new FastQueue<Integer>();
	
		queue1.enqueue("neworleans");
		queue1.enqueue("tampabay");
		queue1.enqueue("carolina");
		queue1.enqueue("atlanta");
		
		for(int x=1;x<10;x++) {
			queue2.enqueue(x);
		}
		
		System.out.println("Queue1 (size=" + queue1.size() + "): " + queue1);
		System.out.println("Queue2 (size=" + queue2.size() + "): " + queue2);
		
		queue1.dequeue();
		queue2.dequeue();
		queue2.dequeue();
		queue2.dequeue();
		
		System.out.println("After dequeue()");
		System.out.println("Queue1 (size=" + queue1.size() + "): " + queue1);
		System.out.println("Queue2 (size=" + queue2.size() + "): " + queue2);
	}

}
