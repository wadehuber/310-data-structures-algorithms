/*
 * Bucket Sort
 * -----------
 * A demonstration of bucket sort from the "Sorting in Linear Time" notes.
 *
 * Bucket sort assumes the input is real numbers uniformly distributed over
 * [0, 1).  It divides that range into n equal buckets, drops each element
 * into the bucket for its range, sorts each bucket with a simple method
 * (insertion sort works well because buckets stay small), and concatenates.
 *
 * Under the uniform assumption each bucket holds roughly a constant number of
 * elements, giving O(n) expected time.
 *
 * This example sorts uniform [0, 1) scores -- the kind of normalized
 * confidence values the notes mention -- and prints the bucket contents so
 * you can see the distribute-then-concatenate structure.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BucketSort {

    /* Plain insertion sort; fast on the short lists inside each bucket. */
    static void insertionSort(List<Double> values) {
        for (int i = 1; i < values.size(); i++) {
            double key = values.get(i);
            int j = i - 1;
            while (j >= 0 && values.get(j) > key) {
                values.set(j + 1, values.get(j));
                j -= 1;
            }
            values.set(j + 1, key);
        }
    }

    /*
     * Return a sorted copy of A, where every element is in [0, 1).
     * Uses n buckets so that element x lands in bucket floor(n * x).
     */
    static double[] bucketSort(double[] A, boolean showBuckets) {
        int n = A.length;
        if (n == 0) {
            return new double[0];
        }

        List<List<Double>> buckets = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            buckets.add(new ArrayList<>());
        }

        // Distribute: bucket index scales with the value (input is in [0, 1)).
        for (double x : A) {
            int index = (int) (n * x);
            if (index == n) {   // guard the x == 1.0 edge if it ever appears
                index = n - 1;
            }
            buckets.get(index).add(x);
        }

        // Sort each bucket, then concatenate in order.
        double[] result = new double[n];
        int pos = 0;
        for (int i = 0; i < n; i++) {
            List<Double> bucket = buckets.get(i);
            insertionSort(bucket);
            if (showBuckets) {
                System.out.printf("  bucket %d [%.2f, %.2f): %s%n",
                        i, (double) i / n, (double) (i + 1) / n, bucket);
            }
            for (double x : bucket) {
                result[pos++] = x;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        double[] scores = {0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68};

        System.out.println("Input scores: " + Arrays.toString(scores));
        System.out.println("Buckets:");
        double[] result = bucketSort(scores, true);
        System.out.println("Bucket sorted:  " + Arrays.toString(result));

        double[] sorted = scores.clone();
        Arrays.sort(sorted);
        System.out.println("Library sorted: " + Arrays.toString(sorted));
    }
}
