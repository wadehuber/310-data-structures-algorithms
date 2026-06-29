# Greedy Algorithms

Code examples from **Module 12 — Greedy Algorithms** (CLRS Ch. 15).
A greedy algorithm makes the locally optimal choice at each step
and never revisits it. This works only when the problem has the
**greedy-choice property** (a global optimum can be reached by local choices) and
**optimal substructure**. Each example shows a greedy rule and why it is safe.

## What each shows

- **Offline caching** — the greedy "evict the page used farthest in the future"
  rule (Belady's MIN) is provably optimal *because* it can see the whole request
  sequence. Comparing it to online LRU on the same input makes the value of
  future knowledge concrete.
- **Huffman coding** — frequent symbols get short codewords. The greedy
  merge-two-smallest rule yields an optimal prefix code; the program shows the
  codewords, the bit savings vs. a fixed-width code, and an unambiguous decode.
- **Activity selection** — sorting by finish time and taking each compatible
  activity is the textbook greedy-choice argument; Prolog states it declaratively.

## Running

```bash
# Offline caching
python3 offline_caching.py
g++ -std=c++17 -O2 offline_caching.cpp -o offline_caching && ./offline_caching

# Huffman
javac Huffman.java && java Huffman

# Activity selection (SWI-Prolog)
swipl -g main -t halt activity_selection.pl
# SICStus:  sicstus -l activity_selection.pl --goal "main."
```

## Where each ties back to the notes

- *An Activity-Selection Problem* → `activity_selection.pl`
- *Huffman Codes* (prefix codes, min-heap construction) → `Huffman.java`
- *Offline Caching* (farthest-in-future / Belady's MIN, online vs. offline) → `offline_caching.py`, `offline_caching.cpp`
