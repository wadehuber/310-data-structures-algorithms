/*
 * Radix Sort (LSD)
 * ----------------
 * A demonstration of least-significant-digit radix sort from the
 * "Sorting in Linear Time" notes.
 *
 * Radix sort extends counting sort to multi-digit numbers by sorting one
 * digit at a time, from least significant to most significant.  Each pass
 * uses a *stable* counting sort as its subroutine, so the ordering achieved
 * by earlier (lower) digits survives later passes.
 *
 * For d-digit numbers in base r it runs in Theta(d * (n + r)) time -- linear
 * in the input when the number of digits d is small or constant.
 *
 * This example sorts fixed-width integer keys (think hashed feature ids or
 * quantized values) in base 10 so you can print the array after each digit
 * pass and watch it converge.
 */

import java.util.Arrays;

public class RadixSort {

    /*
     * Stable counting sort of A using the digit selected by exp.
     *
     * exp is a power of base: exp=1 sorts by the ones digit, exp=10 by the
     * tens digit, and so on.  Stability here is what makes the multi-pass
     * radix sort correct.
     */
    static int[] countingSortByDigit(int[] A, int exp, int base) {
        int n = A.length;
        int[] C = new int[base];
        int[] B = new int[n];

        // Count occurrences of each digit value (0..base-1).
        for (int value : A) {
            int digit = (value / exp) % base;
            C[digit] += 1;
        }

        // Cumulative sums -> ending positions.
        for (int d = 1; d < base; d++) {
            C[d] += C[d - 1];
        }

        // Place right-to-left to preserve stability.
        for (int j = n - 1; j >= 0; j--) {
            int digit = (A[j] / exp) % base;
            C[digit] -= 1;
            B[C[digit]] = A[j];
        }

        return B;
    }

    /*
     * Return a sorted copy of A (non-negative integers), one digit pass at a
     * time.  Set trace=true to print the array after each pass.
     */
    static int[] radixSort(int[] A, int base, boolean trace) {
        if (A.length == 0) {
            return new int[0];
        }

        int[] result = A.clone();
        int maxValue = result[0];
        for (int v : result) {
            if (v > maxValue) {
                maxValue = v;
            }
        }

        int exp = 1;
        while (maxValue / exp > 0) {
            result = countingSortByDigit(result, exp, base);
            if (trace) {
                String place = (exp == 1) ? "ones" : (exp + "s");
                System.out.printf("  after %6s digit: %s%n", place, Arrays.toString(result));
            }
            exp *= base;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] keys = {329, 457, 657, 839, 436, 720, 355, 8, 90, 3};

        System.out.println("Input keys: " + Arrays.toString(keys));
        System.out.println("Radix sort passes (LSD -> MSD):");
        int[] result = radixSort(keys, 10, true);
        System.out.println("Radix sorted:   " + Arrays.toString(result));

        int[] sorted = keys.clone();
        Arrays.sort(sorted);
        System.out.println("Library sorted: " + Arrays.toString(sorted));
    }
}
