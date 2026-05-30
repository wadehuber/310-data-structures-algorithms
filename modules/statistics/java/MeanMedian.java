/*
 * Mean vs. Median: A Robustness Illustration
 * -------------------------------------------
 * A demonstration of the "Robust Statistics" idea from the "Medians & Order
 * Statistics" notes:
 *
 *     Mean is sensitive to values.  Median is sensitive only to order.
 *
 * This program computes both, then injects a single extreme value and
 * recomputes, so you can see the mean lurch toward the outlier while the
 * median barely moves.  That is the whole point of calling the median
 * *robust*: a small fraction of extreme values cannot significantly change it.
 *
 * (Computing the median here uses a sort for clarity.  As the notes explain --
 * and as SelectMedians.java / RandSelect.java show -- the median can actually
 * be found in Theta(n) time without fully sorting.)
 */

import java.util.Arrays;

public class MeanMedian {

    /* Arithmetic mean: sum of values divided by count. Uses every value. */
    static double mean(double[] data) {
        double sum = 0.0;
        for (double x : data) sum += x;
        return sum / data.length;
    }

    /*
     * Middle value after ordering.  Depends only on relative order, not on
     * how large the extreme values are.
     */
    static double median(double[] data) {
        double[] s = data.clone();
        Arrays.sort(s);
        int n = s.length;
        int mid = n / 2;
        if (n % 2 == 1) {
            return s[mid];
        }
        return (s[mid - 1] + s[mid]) / 2.0;
    }

    static void report(String label, double[] data) {
        System.out.println(label);
        System.out.println("  data:   " + Arrays.toString(data));
        System.out.printf("  mean:   %.2f%n", mean(data));
        System.out.printf("  median: %.2f%n", median(data));
        System.out.println();
    }

    public static void main(String[] args) {
        // Server response times in milliseconds: tightly clustered, no outlier.
        double[] clean = {102, 98, 105, 99, 101, 103, 100, 97, 104};
        report("Clean readings:", clean);

        // One request hit a stall (a 4000 ms spike). Same data plus one outlier.
        double[] withOutlier = Arrays.copyOf(clean, clean.length + 1);
        withOutlier[clean.length] = 4000;
        report("With one extreme outlier added:", withOutlier);

        double baseMean = mean(clean), baseMedian = median(clean);
        double outMean = mean(withOutlier), outMedian = median(withOutlier);
        System.out.println("Effect of the single outlier:");
        System.out.printf("  mean   moved by %8.2f ms  (chases the outlier)%n",
                outMean - baseMean);
        System.out.printf("  median moved by %8.2f ms  (stays put -> robust)%n",
                outMedian - baseMedian);
    }
}
