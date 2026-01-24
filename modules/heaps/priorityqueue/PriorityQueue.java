package priorityqueue;
import heaps.linkedheap.*;

/**
 * PriorityQueue implements a priority queue using a heap.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class PriorityQueue<T>
{
	
	LinkedHeap<PrioritizedObject<T>> pqueue = new LinkedHeap<PrioritizedObject<T>>();
	
	/**
	 * Creates an empty priority queue.
	 */
	public PriorityQueue() 
	{	
	}

	/**
	 * Adds the given element to this PriorityQueue.
	 *
	 * @param object the element to be added to the priority queue
	 * @param priority the integer priority of the element to be added
	 */
	public void addElement(T object, int priority) 
	{
		PrioritizedObject<T> obj = new PrioritizedObject<T>(object, priority);
		pqueue.addElement(obj);
	}

	/**
	 * Removes the next highest priority element from this priority 
	 * queue and returns a reference to it.
	 *
	 * @return a reference to the next highest priority element in this queue
	 */
	public T removeNext() 
	{
		PrioritizedObject<T> obj = (PrioritizedObject<T>)pqueue.removeMin();
		return obj.getElement();
	}
	
	public int size( ) {
		return pqueue.size();
	}

	public boolean isEmpty() {
		return pqueue.isEmpty();
	}
}