/*
 * Huffman Coding  (CSC310 Module 12 - Greedy Algorithms)
 * ======================================================
 *
 * Greedy rule: repeatedly remove the two lowest-frequency nodes from a min-heap,
 * merge them under a new parent whose frequency is their sum, and reinsert.  The
 * result is an optimal prefix code (left = 0, right = 1).
 *
 *   javac Huffman.java && java Huffman
 *
 * Running time: O(n log n) with a binary heap.
 */
import java.util.*;

public class Huffman {

    static class Node {
        char ch;          // valid only for leaves
        int freq;
        Node left, right;
        Node(char ch, int freq) { this.ch = ch; this.freq = freq; }
        Node(Node l, Node r) { freq = l.freq + r.freq; left = l; right = r; }
        boolean isLeaf() { return left == null && right == null; }
    }

    static void buildCodes(Node n, String code, Map<Character, String> out) {
        if (n.isLeaf()) {
            out.put(n.ch, code.isEmpty() ? "0" : code); // single-symbol edge case
            return;
        }
        buildCodes(n.left, code + "0", out);
        buildCodes(n.right, code + "1", out);
    }

    static Node huffman(Map<Character, Integer> freq) {
        // Order by frequency; break ties by symbol so the tree is deterministic.
        PriorityQueue<Node> pq = new PriorityQueue<>(
            (a, b) -> a.freq != b.freq ? a.freq - b.freq : a.ch - b.ch);
        for (var e : freq.entrySet()) pq.add(new Node(e.getKey(), e.getValue()));
        while (pq.size() > 1) {
            Node x = pq.poll();   // lowest
            Node y = pq.poll();   // next lowest
            Node merged = new Node(x, y);
            merged.ch = (char) Math.min(x.ch, y.ch); // for stable tie-breaking
            pq.add(merged);
        }
        return pq.poll();
    }

    public static void main(String[] args) {
        // Classic CLRS frequencies; optimal encoding is 224 bits.
        Map<Character, Integer> freq = new LinkedHashMap<>();
        freq.put('a', 45); freq.put('b', 13); freq.put('c', 12);
        freq.put('d', 16); freq.put('e', 9);  freq.put('f', 5);

        Node root = huffman(freq);
        Map<Character, String> codes = new TreeMap<>();
        buildCodes(root, "", codes);

        System.out.println("Symbol  Freq  Codeword");
        int totalBits = 0, totalFreq = 0;
        for (var e : freq.entrySet()) {
            String code = codes.get(e.getKey());
            System.out.printf("  %c     %3d   %s%n", e.getKey(), e.getValue(), code);
            totalBits += e.getValue() * code.length();
            totalFreq += e.getValue();
        }
        System.out.println();
        System.out.println("Huffman total : " + totalBits + " bits");
        System.out.println("Fixed 3-bit   : " + (totalFreq * 3) + " bits");

        // Encode / decode round-trip demo.
        String text = "abcdef";
        StringBuilder enc = new StringBuilder();
        for (char c : text.toCharArray()) enc.append(codes.get(c));
        StringBuilder dec = new StringBuilder();
        Node cur = root;
        for (char bit : enc.toString().toCharArray()) {
            cur = (bit == '0') ? cur.left : cur.right;
            if (cur.isLeaf()) { dec.append(cur.ch); cur = root; }
        }
        System.out.println();
        System.out.println("\"" + text + "\" -> " + enc + " -> \"" + dec + "\"");
    }
}
