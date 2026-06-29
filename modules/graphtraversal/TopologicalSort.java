/*
 * Topological Sort  (CSC310 Module 7 - Graph Algorithms)
 * ======================================================
 *
 * DFS method: output vertices in DECREASING finish time (prepend on finish).
 * A back edge (a GRAY neighbor) means the graph has a cycle and no order exists.
 *
 *   javac TopologicalSort.java && java TopologicalSort
 *
 * Time: O(|V| + |E|).
 */
import java.util.*;

public class TopologicalSort {

    static final int WHITE = 0, GRAY = 1, BLACK = 2;
    static Map<String, Integer> color = new HashMap<>();
    static Deque<String> order = new ArrayDeque<>();   // prepend on finish
    static boolean hasCycle = false;

    static void dfsVisit(String u, Map<String, List<String>> adj) {
        color.put(u, GRAY);
        for (String v : adj.get(u)) {
            int c = color.get(v);
            if (c == WHITE) dfsVisit(v, adj);
            else if (c == GRAY) hasCycle = true;       // back edge -> cycle
        }
        color.put(u, BLACK);
        order.addFirst(u);
    }

    static List<String> topologicalSort(Map<String, List<String>> adj) {
        for (String u : adj.keySet()) color.put(u, WHITE);
        for (String u : adj.keySet())
            if (color.get(u) == WHITE) dfsVisit(u, adj);
        return hasCycle ? null : new ArrayList<>(order);
    }

    public static void main(String[] args) {
        // CLRS "getting dressed" DAG (not used in any CSC310 assignment).
        Map<String, List<String>> adj = new LinkedHashMap<>();
        adj.put("undershorts", List.of("pants", "shoes"));
        adj.put("pants",       List.of("belt", "shoes"));
        adj.put("belt",        List.of("jacket"));
        adj.put("shirt",       List.of("belt", "tie"));
        adj.put("tie",         List.of("jacket"));
        adj.put("jacket",      List.of());
        adj.put("socks",       List.of("shoes"));
        adj.put("shoes",       List.of());
        adj.put("watch",       List.of());

        List<String> result = topologicalSort(adj);
        if (result == null) {
            System.out.println("Graph has a cycle: no topological ordering exists.");
        } else {
            System.out.println("A valid topological order:");
            System.out.println("  " + String.join(" -> ", result));
        }
    }
}
