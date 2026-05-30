/*
 * Deterministic Selection (Median of Medians)
 * --------------------------------------------
 * The SELECT algorithm from the "Medians & Order Statistics" notes -- the
 * worst-case O(n) selection algorithm, in contrast to RANDOMIZED-SELECT
 * (RandSelect.java), which is only O(n) *expected*.
 *
 * The trick is choosing a provably good pivot instead of a random one:
 *   1. Split the elements into groups of 5.
 *   2. Find each group's median (by sorting the tiny group).
 *   3. Recursively SELECT the median OF those medians.
 *   4. Partition around that "median of medians" -- it is guaranteed to be
 *      far enough from the extremes that each recursive call shrinks the
 *      problem by a constant fraction, which keeps the worst case linear.
 *
 * As the notes point out, this guarantee comes with larger constant factors,
 * so in practice quickselect is usually preferred -- a classic case of
 * theoretical optimality not matching real-world speed.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SelectMedians {

    /* Return the i-th smallest element of `data` (1-based) in worst-case O(n). */
    static int medianOfMediansSelect(List<Integer> data, int i) {
        int n = data.size();
        if (n <= 5) {
            List<Integer> small = new ArrayList<>(data);
            Collections.sort(small);
            return small.get(i - 1);
        }

        // Step 1-2: median of each group of 5.
        List<Integer> medians = new ArrayList<>();
        for (int start = 0; start < n; start += 5) {
            List<Integer> group = new ArrayList<>(data.subList(start, Math.min(start + 5, n)));
            Collections.sort(group);
            medians.add(group.get((group.size() - 1) / 2));
        }

        // Step 3: median of the medians (recursively).
        int pivot = medianOfMediansSelect(medians, (medians.size() + 1) / 2);

        // Step 4: partition around the pivot and recurse into one side only.
        List<Integer> less = new ArrayList<>();
        List<Integer> equal = new ArrayList<>();
        List<Integer> greater = new ArrayList<>();
        for (int x : data) {
            if (x < pivot) less.add(x);
            else if (x > pivot) greater.add(x);
            else equal.add(x);
        }

        if (i <= less.size()) {
            return medianOfMediansSelect(less, i);
        } else if (i <= less.size() + equal.size()) {
            return pivot;                                   // pivot is the answer
        } else {
            int newI = i - less.size() - equal.size();
            return medianOfMediansSelect(greater, newI);
        }
    }

    static List<Integer> toList(int[] a) {
        List<Integer> list = new ArrayList<>();
        for (int x : a) list.add(x);
        return list;
    }

    public static void main(String[] args) {
        int[] A = {25, 3, 41, 17, 9, 38, 2, 14, 30, 7, 22, 11, 36, 5, 19, 28, 1, 33, 16};
        System.out.println("Array: " + Arrays.toString(A));
        System.out.println();

        int[] ordered = A.clone();
        Arrays.sort(ordered);

        int n = A.length;
        int[] ranks = {1, n / 2 + 1, n};
        for (int i : ranks) {
            int got = medianOfMediansSelect(toList(A), i);
            String label = (i == n / 2 + 1) ? "median" : (i == 1 ? "min" : "max");
            System.out.printf("%2dth smallest (%6s): %d   (sorted check: %d)%n",
                    i, label, got, ordered[i - 1]);
        }

        System.out.println();
        // Confirm it agrees with a full sort for all ranks.
        boolean allMatch = true;
        for (int i = 1; i <= n; i++) {
            if (medianOfMediansSelect(toList(A), i) != ordered[i - 1]) {
                allMatch = false;
                break;
            }
        }
        System.out.println("Matches sorted order for every rank: " + allMatch);
    }
}
