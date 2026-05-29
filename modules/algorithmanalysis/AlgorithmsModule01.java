/*
 * CSC310 — Module 01: Algorithm Analysis
 * Sample implementations in Java.
 *
 * Algorithms covered:
 *   - Linear Search          O(n) worst
 *   - Binary Search          O(log n) worst (iterative & recursive)
 *   - Insertion Sort         O(n^2) worst, O(n) best   (CLRS Fig. 2.1)
 *   - Merge Sort             Θ(n log n)                (CLRS §2.3)
 *   - Towers of Hanoi        Θ(2^n)
 *   - Recursive vs iterative factorial (Θ(n) stack vs Θ(1) stack)
 *   - Empirical timing demo connecting asymptotic to wall-clock
 *
 * The race-condition example is in RaceConditionDemo.java so it can be
 * compiled and run separately.
 *
 * Compile: javac AlgorithmsModule01.java
 * Run    : java  AlgorithmsModule01
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class AlgorithmsModule01 {

    // ---------------------------------------------------------------------
    // 1. LINEAR SEARCH
    // Best Θ(1), worst/avg Θ(n), space Θ(1)
    // ---------------------------------------------------------------------
    public static SearchResult linearSearch(int[] arr, int target) {
        long comparisons = 0;
        for (int i = 0; i < arr.length; i++) {
            comparisons++;                  // key processing step
            if (arr[i] == target) return new SearchResult(i, comparisons);
        }
        return new SearchResult(-1, comparisons);
    }

    // ---------------------------------------------------------------------
    // 2. BINARY SEARCH — requires sorted input (a critical assumption!)
    // Best Θ(1), worst Θ(log n). Iterative is Θ(1) space; recursive Θ(log n).
    // ---------------------------------------------------------------------
    public static SearchResult binarySearchIterative(int[] arr, int target) {
        long comparisons = 0;
        int low = 0, high = arr.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;   // avoids overflow vs (low+high)/2
            comparisons++;
            if (arr[mid] == target) return new SearchResult(mid, comparisons);
            if (arr[mid] < target) low = mid + 1;
            else                   high = mid - 1;
        }
        return new SearchResult(-1, comparisons);
    }

    public static SearchResult binarySearchRecursive(int[] arr, int target) {
        return binarySearchRecursiveHelper(arr, target, 0, arr.length - 1, 0);
    }

    private static SearchResult binarySearchRecursiveHelper(
            int[] arr, int target, int low, int high, long cmp) {
        if (low > high) return new SearchResult(-1, cmp);
        int mid = low + (high - low) / 2;
        cmp++;
        if (arr[mid] == target) return new SearchResult(mid, cmp);
        if (arr[mid] < target)
            return binarySearchRecursiveHelper(arr, target, mid + 1, high, cmp);
        return binarySearchRecursiveHelper(arr, target, low, mid - 1, cmp);
    }

    // ---------------------------------------------------------------------
    // 3. INSERTION SORT (CLRS Figure 2.1, translated to 0-based indexing)
    // Best  Θ(n)   — already sorted
    // Worst Θ(n^2) — reverse sorted
    // Space Θ(1)   — in-place
    // ---------------------------------------------------------------------
    public static long insertionSort(int[] A) {
        long comparisons = 0;
        // CLRS: for j = 2 to A.length   (1-based)
        // Java: for j = 1 to A.length-1 (0-based)
        for (int j = 1; j < A.length; j++) {
            int key = A[j];
            int i = j - 1;
            while (i >= 0) {
                comparisons++;
                if (A[i] <= key) break;
                A[i + 1] = A[i];
                i--;
            }
            A[i + 1] = key;
        }
        return comparisons;
    }

    // ---------------------------------------------------------------------
    // 4. MERGE SORT — divide and conquer
    // T(n) = 2 T(n/2) + Θ(n)  →  Θ(n log n)
    // Auxiliary space Θ(n)
    // ---------------------------------------------------------------------
    public static long mergeSort(int[] A) {
        long[] comparisons = {0};
        int[] aux = new int[A.length];
        mergeSortHelper(A, aux, 0, A.length - 1, comparisons);
        return comparisons[0];
    }

    private static void mergeSortHelper(int[] A, int[] aux, int lo, int hi,
                                        long[] comparisons) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        mergeSortHelper(A, aux, lo, mid, comparisons);
        mergeSortHelper(A, aux, mid + 1, hi, comparisons);
        merge(A, aux, lo, mid, hi, comparisons);
    }

    private static void merge(int[] A, int[] aux, int lo, int mid, int hi,
                              long[] comparisons) {
        // Copy A[lo..hi] into aux[lo..hi]
        for (int k = lo; k <= hi; k++) aux[k] = A[k];

        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; k++) {
            if      (i > mid)              A[k] = aux[j++];
            else if (j > hi)               A[k] = aux[i++];
            else {
                comparisons[0]++;
                if (aux[j] < aux[i]) A[k] = aux[j++];
                else                 A[k] = aux[i++];
            }
        }
    }

    // ---------------------------------------------------------------------
    // 5. TOWERS OF HANOI
    // T(n) = 2 T(n-1) + 1  →  T(n) = 2^n - 1     i.e.  Θ(2^n)
    // Call-stack depth Θ(n)
    // ---------------------------------------------------------------------
    public static List<int[]> towersOfHanoi(int n) {
        List<int[]> moves = new ArrayList<>();
        hanoi(n, 'A', 'C', 'B', moves);
        return moves;
    }

    private static void hanoi(int n, char from, char to, char aux,
                              List<int[]> moves) {
        if (n == 1) { moves.add(new int[]{from, to}); return; }
        hanoi(n - 1, from, aux, to, moves);
        moves.add(new int[]{from, to});
        hanoi(n - 1, aux, to, from, moves);
    }

    // ---------------------------------------------------------------------
    // 6. RECURSIVE vs ITERATIVE — same Θ(n) time, different stack space
    // ---------------------------------------------------------------------
    public static long factorialRecursive(int n) {
        if (n <= 1) return 1L;
        return n * factorialRecursive(n - 1);     // Θ(n) stack frames
    }

    public static long factorialIterative(int n) {
        long result = 1;
        for (int k = 2; k <= n; k++) result *= k; // Θ(1) extra space
        return result;
    }

    // ---------------------------------------------------------------------
    // 7. EMPIRICAL GROWTH DEMO
    // ---------------------------------------------------------------------
    private static void growthDemo() {
        // JIT warm-up: the HotSpot compiler optimizes hot methods after
        // ~10K invocations. Without warm-up the first row is misleadingly
        // slow because we're measuring interpreter speed.
        int[] warm = new int[500];
        for (int rep = 0; rep < 5; rep++) {
            for (int i = 0; i < warm.length; i++) warm[i] = warm.length - i;
            insertionSort(warm);
            for (int i = 0; i < warm.length; i++) warm[i] = warm.length - i;
            mergeSort(warm);
        }

        System.out.printf("%8s | %14s | %10s | %9s%n",
                "n", "insertion (s)", "merge (s)", "ins/merge");
        System.out.println("-".repeat(55));
        for (int n : new int[]{1_000, 2_000, 4_000, 8_000}) {
            int[] worstIns = new int[n];
            for (int i = 0; i < n; i++) worstIns[i] = n - i;       // reversed
            int[] worstMrg = worstIns.clone();

            long t0 = System.nanoTime();
            insertionSort(worstIns);
            double tIns = (System.nanoTime() - t0) / 1e9;

            t0 = System.nanoTime();
            mergeSort(worstMrg);
            double tMrg = (System.nanoTime() - t0) / 1e9;

            System.out.printf("%8d | %14.4f | %10.4f | %8.1fx%n",
                    n, tIns, tMrg, tIns / Math.max(tMrg, 1e-9));
        }
    }

    // ---------------------------------------------------------------------
    // Demo harness
    // ---------------------------------------------------------------------
    public static void main(String[] args) {
        System.out.println("=== Linear vs Binary Search ===");
        int n = 1_000_000;
        int[] sortedData = new int[n];
        for (int i = 0; i < n; i++) sortedData[i] = i + 1;
        int target = 987_654;

        SearchResult lin = linearSearch(sortedData, target);
        SearchResult bin = binarySearchIterative(sortedData, target);
        System.out.printf("Linear search comparisons : %,d%n", lin.comparisons);
        System.out.printf("Binary search comparisons : %,d  (log2 n ≈ %.1f)%n",
                bin.comparisons, Math.log(n) / Math.log(2));

        System.out.println("\n=== Insertion Sort: best vs worst ===");
        int[] sortedIn = new int[1000];
        int[] reversedIn = new int[1000];
        for (int i = 0; i < 1000; i++) { sortedIn[i] = i + 1; reversedIn[i] = 1000 - i; }
        System.out.printf("Sorted  (best)   comparisons: %,7d   ≈ n - 1 = 999%n",
                insertionSort(sortedIn));
        System.out.printf("Reverse (worst)  comparisons: %,7d   ≈ n(n-1)/2 = %,d%n",
                insertionSort(reversedIn), 1000 * 999 / 2);

        System.out.println("\n=== Merge Sort ===");
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 1000; i++) list.add(i);
        Collections.shuffle(list, new Random(42));
        int[] arr = list.stream().mapToInt(Integer::intValue).toArray();
        long cmp = mergeSort(arr);
        System.out.printf("Merge sort comparisons on n=1000: %,d  (n log2 n ≈ %,d)%n",
                cmp, (int) (1000 * Math.log(1000) / Math.log(2)));
        assert isSorted(arr);

        System.out.println("\n=== Towers of Hanoi ===");
        for (int k : new int[]{1, 3, 5, 10}) {
            int moves = towersOfHanoi(k).size();
            System.out.printf("n = %2d : %,5d moves   (2^n - 1 = %,d)%n",
                    k, moves, (1 << k) - 1);
        }

        System.out.println("\n=== Recursive vs Iterative Factorial ===");
        System.out.printf("factorialIterative(10) = %d%n", factorialIterative(10));
        System.out.printf("factorialRecursive(10) = %d%n", factorialRecursive(10));
        System.out.println("Recursive version uses Θ(n) stack frames.");

        System.out.println("\n=== Empirical Growth Demo ===");
        growthDemo();
    }

    private static boolean isSorted(int[] a) {
        for (int i = 1; i < a.length; i++) if (a[i - 1] > a[i]) return false;
        return true;
    }

    // ---------------------------------------------------------------------
    static class SearchResult {
        final int index;
        final long comparisons;
        SearchResult(int index, long comparisons) {
            this.index = index;
            this.comparisons = comparisons;
        }
        @Override public String toString() {
            return "SearchResult{index=" + index + ", comparisons=" + comparisons + "}";
        }
    }
}
