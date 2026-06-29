/*
 * Optimal Binary Search Tree  (CSC310 Module 11 - Dynamic Programming)
 * ===================================================================
 *
 * Port of optimal_bst.py.  CLRS instance; expected cost = 2.75, root = k2.
 *
 *   javac OptimalBST.java && java OptimalBST
 *
 * Time: Theta(n^3)   Space: Theta(n^2)
 */
public class OptimalBST {

    static int[][] root;

    static double[][] optimalBST(double[] p, double[] q) {
        int n = p.length - 1;             // p is 1-indexed, q is 0-indexed
        double[][] e = new double[n + 2][n + 1];
        double[][] w = new double[n + 2][n + 1];
        root = new int[n + 1][n + 1];

        for (int i = 1; i <= n + 1; i++) {     // empty subtree = one dummy key
            e[i][i - 1] = q[i - 1];
            w[i][i - 1] = q[i - 1];
        }
        for (int len = 1; len <= n; len++) {
            for (int i = 1; i <= n - len + 1; i++) {
                int j = i + len - 1;
                e[i][j] = Double.POSITIVE_INFINITY;
                w[i][j] = w[i][j - 1] + p[j] + q[j];
                for (int r = i; r <= j; r++) {      // try each key as root
                    double cost = e[i][r - 1] + e[r + 1][j] + w[i][j];
                    if (cost < e[i][j]) {
                        e[i][j] = cost;
                        root[i][j] = r;
                    }
                }
            }
        }
        return e;
    }

    static void structure(int i, int j, int depth, String label, StringBuilder sb) {
        String pad = "  ".repeat(depth);
        if (i > j) {
            sb.append(pad).append(label).append(": d").append(j).append("  (dummy leaf)\n");
            return;
        }
        int r = root[i][j];
        sb.append(pad).append(label).append(": k").append(r).append('\n');
        structure(i, r - 1, depth + 1, "left ", sb);
        structure(r + 1, j, depth + 1, "right", sb);
    }

    public static void main(String[] args) {
        double[] p = {0, 0.15, 0.10, 0.05, 0.10, 0.20};   // p[1..5]
        double[] q = {0.05, 0.10, 0.05, 0.05, 0.05, 0.10}; // q[0..5]
        int n = p.length - 1;

        double[][] e = optimalBST(p, q);

        System.out.printf("Expected cost of the optimal BST: %.2f%n", e[1][n]);
        System.out.println("Root of the whole tree           : k" + root[1][n]);
        System.out.println();
        System.out.println("Optimal tree structure:");
        StringBuilder sb = new StringBuilder();
        structure(1, n, 0, "root", sb);
        System.out.print(sb);
    }
}
