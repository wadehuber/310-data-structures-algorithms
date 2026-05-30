/*
 * Randomized Selection (Quickselect)
 * ----------------------------------
 * RANDOMIZED-SELECT from the "Medians & Order Statistics" notes: find the
 * i-th smallest element (1-based) of an array in Theta(n) expected time.
 *
 * It reuses quicksort's partition, but recurses into only the one side that
 * must contain the answer -- so on average it does linear work instead of
 * the n log n a full sort would cost.
 */

import java.util.Arrays;
import java.util.Random;

public class RandSelect {

    private static final Random RNG = new Random();

    /*
     * Chooses a random pivot, swaps it with A[r], then partitions the array
     * around the pivot.  Returns the final pivot index.
     */
    static int randomizedPartition(int[] A, int p, int r) {
        int pivotIndex = p + RNG.nextInt(r - p + 1);
        int tmp = A[pivotIndex];
        A[pivotIndex] = A[r];
        A[r] = tmp;
        return partition(A, p, r);
    }

    /* Standard Lomuto partition scheme. */
    static int partition(int[] A, int p, int r) {
        int pivot = A[r];
        int i = p - 1;

        for (int j = p; j < r; j++) {
            if (A[j] <= pivot) {
                i += 1;
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }

        int tmp = A[i + 1];
        A[i + 1] = A[r];
        A[r] = tmp;
        return i + 1;
    }

    /* Returns the i-th smallest element of A (i is 1-based). */
    static int randomizedSelect(int[] A, int i) {
        return randomizedSelectRange(A, 0, A.length - 1, i);
    }

    /* Returns the i-th smallest element of A[p..r] (i is 1-based). */
    static int randomizedSelectRange(int[] A, int p, int r, int i) {
        if (p == r) {
            return A[p];
        }

        int q = randomizedPartition(A, p, r);
        int k = q - p + 1;          // rank of pivot within subarray

        if (i == k) {
            return A[q];
        } else if (i < k) {
            return randomizedSelectRange(A, p, q - 1, i);
        } else {
            return randomizedSelectRange(A, q + 1, r, i - k);
        }
    }

    public static void main(String[] args) {
        int[] A = {13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11};
        int i = 5;  // Find the 5th smallest element

        System.out.println("Original array: " + Arrays.toString(A));

        // randomizedSelect rearranges its argument, so pass a copy.
        int result = randomizedSelect(A.clone(), i);
        System.out.println(i + "th smallest element: " + result);

        // Verification.
        int[] sortedA = A.clone();
        Arrays.sort(sortedA);
        System.out.println("Sorted array: " + Arrays.toString(sortedA));
        System.out.println("Check: " + sortedA[i - 1]);
    }
}
