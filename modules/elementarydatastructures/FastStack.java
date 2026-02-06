package videoexamples.stacksqueues.csc205;

import videoexamples.stacksqueues.jsjf.StackADT;

public class FastStack<T> implements StackADT<T> {

	LinkedList<T> elements;
	
	public FastStack() {
		super();
		this.elements = new LinkedList<T>();
	}

	@Override
	public void push(T element) {
		elements.addToFront(element);
	}

	@Override
	public T pop() {
		return elements.removeFirst();
	}

	@Override
	public T peek() {
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
		String ret = "top-> ";
		for(T ele : elements) {
			ret += ele + " ";
		}
		return ret;
	}


}
