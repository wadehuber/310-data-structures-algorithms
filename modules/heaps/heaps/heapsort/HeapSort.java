package heaps.heapsort;
// The methods in this package are adapted from the code provided with:
//   Java Foundations (2nd & 3rd ed) by  Lewis, DePasquale, & Chase
//   Algorithms (4th ed) by Sedgewick & Wayne

import heaps.linkedheap.LinkedHeap;

public class HeapSort {

	public static <T> void heapSort(T[] data) 
	{
		LinkedHeap<T> heap = new LinkedHeap<T>();

		// copy the array into a heap 
		for (int i = 0; i < data.length; i++)
			heap.addElement(data[i]);

		// place the sorted elements back into the array 
		int count = 0;
		while (!(heap.isEmpty()))
		{
			data[count] = heap.removeMin();
			count++;
		}
	}

}
