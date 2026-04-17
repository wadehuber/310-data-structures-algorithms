# Randomized Algorithms

## Other Videos

[CMU 15-251: Great Ideas in Theoretical Computer Science: Randomized Algorithms 2016](https://www.youtube.com/watch?v=V_4oQMKDecg)

## Learning Resources

- **CLRS Chapter 7**: Quicksort and randomization
- **CLRS Chapter 31**: Number-Theoretic Algorithms and primality testing
- **Probabilistic Method**: Understanding error bounds and trial requirements

## Example Code

## Algorithms Included

### 1. **Fermat Primality Test** (`fermattest.py`, `fermattest.cpp`)

A probabilistic algorithm for testing primality based on **Fermat's Little Theorem**:

- For a prime `n`, `a^(n-1) ≡ 1 (mod n)` for all `1 < a < n`
- Tests the property for `k` random values of `a`
- Returns "definitely composite" or "probably prime"

**Key Features:**

- Time: O(k log³ n) where k = number of trials
- Handles base cases (n ≤ 3)
- Includes efficient modular exponentiation
- Higher trial counts increase confidence in results

**Example Output:**

```
10: composite
17: probably prime
21: composite
122: composite
561: composite (Carmichael number - passes Fermat with low probability)
997: probably prime
```

### 2. **Randomized Quicksort** (`quicksort.py`)

A divide-and-conquer sorting algorithm with **random pivot selection**:

- Randomly selects a pivot element
- Partitions into elements: less than, equal to, greater than pivot
- Recursively sorts partitions and combines results

**Key Features:**

- Expected Time: O(n log n)
- Worst Case: O(n²) (unlikely with random pivot)
- Avoids O(n²) worst-case on pre-sorted data (unlike deterministic pivot selection)
- Handles duplicates naturally with three-way partition

## File Structure

```text
.
├── fermattest.py       # Fermat test in Python
├── fermattest.cpp      # Fermat test in C++
├── quicksort.py        # Randomized quicksort in Python
└── README.md           # This file
```

## Building and Running

### Python

```bash
python fermattest.py
python quicksort.py
```

### C++

```bash
g++ -o fermattest fermattest.cpp
./fermattest
```

## Notes

- The Fermat test has a non-trivial error probability; multiple trials reduce this
- Carmichael numbers (e.g., 561) can fool basic Fermat tests; consider Miller-Rabin for production
- Randomized quicksort performance depends on random pivot quality; in adversarial cases, consider hybrid approaches
