package quicksort;
// The methods in this package are adapted from the code provided with:
//   Java Foundations (2nd & 3rd ed) by  Lewis, DePasquale, & Chase
//   Algorithms (4th ed) by Sedgewick & Wayne

import java.util.Random;

public class QuickSort {

	// Helper methods
	// These operations will occur multiple times in our sorting methods,
	//   so we add methods for them here

	private static <T extends Comparable<T>> boolean less_than(T a, T b) {
		return (a.compareTo(b) < 0);
	}
	private static <T extends Comparable<T>> boolean less_than_equal(T a, T b) {
		return (a.compareTo(b) <= 0);
	}
	private static <T extends Comparable<T>> boolean greater_than(T a, T b) {
		return (a.compareTo(b) > 0);
	}
	private static void swap(Object[] a, int ii, int jj) {
		Object swap = a[ii];
		a[ii] = a[jj];
		a[jj] = swap;
	}
	public static <T extends Comparable<T>> 
	boolean isSorted(T[]data){
		return isSorted(data, 0, data.length-1);
	}
	public static <T extends Comparable<T>> 
	boolean isSorted(T[]data, int min, int max){
		for (int ii=min+1; ii<=max; ii++) {
			if (less_than(data[ii], data[ii-1]))
				return false;
		}
		return true;
	}

	public static <T extends Comparable<T>> 
	void quickSort(T[] data) {
		quickSort(data, 0, data.length-1);
	}

	private static <T extends Comparable<T>> 
	void quickSort(T[] data, int min, int max) {
		if (min < max)
		{
			// create partitions
			int indexofpartition = partition(data, min, max);
			
			// sort the left partition (lower values)
			quickSort(data, min, indexofpartition - 1);
			
			// sort the right partition (higher values)
			quickSort(data, indexofpartition + 1, max);
		}
	}

	private static <T extends Comparable<T>> 
	int partition(T[] data, int min, int max) {
		T partitionelement;
		int left, right;
		int middle = min + ((max - min) / 2);
		
		// use the middle data value as the partition element
		partitionelement = data[middle];
		// move it out of the way for now
		swap(data, middle, min);
		
		left = min;
		right = max;
		
		while (left < right)
		{
			// search for an element that is > the partition element
			while (left < right && less_than_equal(data[left],partitionelement))
				left++;
			
			// search for an element that is < the partition element
			while (greater_than(data[right], partitionelement))
				right--;
			
			// swap the elements
			if (left < right)
				swap(data, left, right);
		}
		
		// move the partition element into place
		swap(data, min, right);
		
		return right;
	}

	
	public static void main(String args[]) {
		Integer[] a = new Integer[100];
		Random rand = new Random();
		int failures = 0;
		
		for (int kk=0; kk<5; kk++) {
		    for (int ii=0;ii<a.length;ii++) {
		    	a[ii] = rand.nextInt(1000);
		    }
		    
		    System.out.print("\nUnsorted: ");
		    printArray(a);
		    		    
		    quickSort(a);

			System.out.print("  Sorted: ");
			printArray(a);   
			
			if (!isSorted(a)) {
				System.out.println("Fail!");
				failures++;
			}

		}
		
		System.out.println();
	    if (failures == 0) {
	    	System.out.println("Test successful! (" + failures + " failures)");
	    }
	    else {
	    	System.out.println("Test unsuccessful! (" + failures + " failures)");   	
	    }

	}
	
	public static void printArray(Object[] a) {
		for (int ii=0;ii<a.length;ii++) {
			System.out.print (a[ii] + " ");
		}
		System.out.println();
	}
}
