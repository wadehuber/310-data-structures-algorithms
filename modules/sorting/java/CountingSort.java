/*
 * Counting Sort
 * -------------
 * A demonstration of the stable counting sort described in the
 * "Sorting in Linear Time" notes.
 *
 * Counting sort works when the input is integers in a small, known range
 * {0, 1, ..., k}.  It runs in Theta(n + k) time, which is linear when k = O(n).
 *
 * This example sorts a list of small integer "class labels" -- the kind of
 * bounded-range data the notes mention (one-hot category indices, histogram
 * bins, discretized features) -- so you can watch the three passes in action.
 */

import java.util.Arrays;

public class CountingSort {

    /*
     * Return a sorted copy of A, where every element is an integer in 0..k.
     *
     * Mirrors the stable pseudocode from the notes:
     *   1. Count occurrences of each value.
     *   2. Turn counts into cumulative end-positions.
     *   3. Place elements right-to-left to keep equal keys stable.
     */
    static int[] countingSort(int[] A, int k) {
        int n = A.length;
        int[] C = new int[k + 1];   // C[v] will count how many times v appears
        int[] B = new int[n];       // output array

        // Pass 1: tally each value.
        for (int value : A) {
            C[value] += 1;
        }

        // Pass 2: cumulative sums -> C[v] is the ending position of value v.
        for (int v = 1; v <= k; v++) {
            C[v] += C[v - 1];
        }

        // Pass 3: walk right-to-left so equal keys keep their original order.
        for (int j = n - 1; j >= 0; j--) {
            int value = A[j];
            C[value] -= 1;
            B[C[value]] = value;
        }

        return B;
    }

    /*
     * Stable counting sort on (key, tag) pairs, keyed by the integer key.
     *
     * The tag carries along unchanged so you can SEE stability: items with
     * the same key come out in the same order they went in.  This stability
     * is exactly the property radix sort relies on.
     */
    static String[] countingSortPairs(int[] keys, String[] tags, int k) {
        int n = keys.length;
        int[] C = new int[k + 1];
        int[] outKeys = new int[n];
        String[] outTags = new String[n];

        for (int key : keys) {
            C[key] += 1;
        }
        for (int v = 1; v <= k; v++) {
            C[v] += C[v - 1];
        }
        for (int j = n - 1; j >= 0; j--) {
            int key = keys[j];
            C[key] -= 1;
            outKeys[C[key]] = key;
            outTags[C[key]] = tags[j];
        }

        String[] formatted = new String[n];
        for (int i = 0; i < n; i++) {
            formatted[i] = "(" + outKeys[i] + ", " + outTags[i] + ")";
        }
        return formatted;
    }

    public static void main(String[] args) {
        // Bounded-range integer labels (values 0..5).
        int[] labels = {3, 0, 5, 2, 3, 1, 0, 4, 2, 3, 5, 1, 0};
        int k = 5;

        System.out.println("Input labels: " + Arrays.toString(labels));
        System.out.println("Counting sorted: " + Arrays.toString(countingSort(labels, k)));

        int[] sorted = labels.clone();
        Arrays.sort(sorted);
        System.out.println("Library sorted:  " + Arrays.toString(sorted));
        System.out.println();

        // Show stability: each pair is (key, arrival_order).
        // After sorting by key, equal keys must stay in arrival order.
        int[] pairKeys = {2, 1, 2, 0, 1, 2};
        String[] pairTags = {"a", "b", "c", "d", "e", "f"};
        System.out.println("Stable sorted: " + Arrays.toString(countingSortPairs(pairKeys, pairTags, 2)));
        System.out.println("Notice the (2, ...) items stay in a, c, f order -> stable.");
    }
}
