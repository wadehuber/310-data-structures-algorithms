package videoexamples.stacksqueues.csc205;

import videoexamples.stacksqueues.jsjf.QueueADT;

public class FastQueue<T> implements QueueADT<T> {
	
	LinkedList<T> elements;

	public FastQueue() {
		super();
		this.elements = new LinkedList<T>();
	}

	@Override
	public void enqueue(T element) {
		elements.addToRear(element);
	}

	@Override
	public T dequeue() {
		return elements.removeFirst();
	}

	@Override
	public T first() {
		return elements.first();
	}

	@Override
	public boolean isEmpty() {
		return elements.isEmpty();
	}

	@Override
	public int size() {
		return elements.size();
	}

	@Override
	public String toString() {
		String ret = "front-> ";
		for (T ele : elements) {
			ret += ele + " ";
		}
		return ret + " <- rear";
	}
}
