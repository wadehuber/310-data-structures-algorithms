# Hash Tables

Code examples from **Module 4B — Hashing & Hash Tables** (CLRS Ch. 11).
A hash table maps a key to a slot via a hash function, giving
expected O(1) insert/search/delete. The two design questions are *how to hash*
(spread keys evenly) and *how to resolve collisions*.

- [Video: Overview of Searching & Hashing](https://youtu.be/lbZ9O7EUrDo) (6:01)

## Examples

| File | Language | What it shows |
|------|----------|---------------|
| [`HashingExample.java`](HashingExample.java) | Java | Writing basic hash functions (original course example). |
| [`hash_function_comparison.py`](hash_function_comparison.py), [`.cpp`](hash_function_comparison.cpp) | Python, C++ | Compares the notes' strategies (division, multiplication, folding, mid-square) vs. a poor first-digit hash on two quality measures: distribution (collisions/empties/longest bucket) and **avalanche** (a good hash flips ~50% of output bits per input-bit change; the weak one ~9%). |
| [`collision_resolution.py`](collision_resolution.py) | Python | Chaining vs. linear / quadratic / double probing: average probes vs. load factor checked against the notes' formulas, primary-clustering measurement, and tombstone deletion. |
| [`hash_table.cpp`](hash_table.cpp), [`hash_table.scm`](hash_table.scm) | C++, Scheme | A reusable separate-chaining hash table that resizes (doubles + rehashes) when the load factor exceeds 0.75. |

## What the measurements show

- **Hash quality** — division, multiplication, folding, and mid-square all
  scatter keys near the ideal collision count; the first-digit hash piles keys
  into a handful of slots. Avalanche separates a real mixing hash (~0.50) from a
  weak one (~0.09).
- **Collision resolution** — chaining tracks 1 + α/2; double hashing tracks
  (1/α)·ln(1/(1−α)); linear probing degrades fast at high load (≈5 probes at
  α = 0.9) because of primary clustering (its longest occupied run is far longer
  than double hashing's). Tombstones let deletion work without breaking probe
  chains.
- **Resizing** — keeping the load factor under a threshold (here 0.75) is what
  preserves expected O(1); the table doubles and rehashes when it's crossed.

## Running

```bash
javac HashingExample.java && java HashingExample

python3 hash_function_comparison.py
g++ -std=c++17 -O2 hash_function_comparison.cpp -o hash_function_comparison && ./hash_function_comparison

python3 collision_resolution.py

g++ -std=c++17 -O2 hash_table.cpp -o hash_table && ./hash_table
guile hash_table.scm        # Scheme (GNU Guile)
```

## Where each ties back to the notes

- *Designing a Hashing Function / Hashing Strategies* → `hash_function_comparison.py`, `.cpp`
- *Resolving Collisions (chaining, linear/quadratic/double probing, tombstones)* → `collision_resolution.py`
- *Hash Table Size / load factor & resizing* → `hash_table.cpp`, `hash_table.scm`
