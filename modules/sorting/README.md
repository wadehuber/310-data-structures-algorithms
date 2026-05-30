# Sorting in Linear Time

Runnable examples that complement the **Module 03A — Sorting in Linear Time**
notes. Comparison sorts are bound by Ω(n log n), but when the input has extra
structure (small integer ranges, fixed-width keys, a known distribution) we can
sort in linear time. Each example demonstrates one of those algorithms
*working*, with output you can read pass-by-pass.

These are illustrations of the concepts only — they are **not** solutions to the
lab or homework questions.

Every example is provided in four languages. They implement the same algorithm
the same way and print the same output, so you can read whichever language you
are most comfortable with.

## Examples

| Algorithm | Demonstrates | Python | Java | C++ | Scheme |
|-----------|--------------|--------|------|-----|--------|
| Counting sort, Θ(n + k) | The three-pass count → cumulate → place structure, plus a stability demo on (key, tag) pairs | [`counting_sort.py`](python/counting_sort.py) | [`CountingSort.java`](java/CountingSort.java) | [`counting_sort.cpp`](cpp/counting_sort.cpp) | [`counting_sort.scm`](scheme/counting_sort.scm) |
| LSD radix sort, Θ(d(n + r)) | Sorting multi-digit integers one digit at a time, printing the array after each digit pass | [`radix_sort.py`](python/radix_sort.py) | [`RadixSort.java`](java/RadixSort.java) | [`radix_sort.cpp`](cpp/radix_sort.cpp) | [`radix_sort.scm`](scheme/radix_sort.scm) |
| Bucket sort, O(n) expected | Distributing uniform [0, 1) values into n buckets, sorting each, and concatenating | [`bucket_sort.py`](python/bucket_sort.py) | [`BucketSort.java`](java/BucketSort.java) | [`bucket_sort.cpp`](cpp/bucket_sort.cpp) | [`bucket_sort.scm`](scheme/bucket_sort.scm) |

Counting sort's stability is what makes radix sort correct, so it is worth
reading first. Each program prints its result next to the language's built-in
sort so you can confirm they agree.

## Directory layout

```(text)
sorting/
├── python/   counting_sort.py   radix_sort.py    bucket_sort.py
├── java/     CountingSort.java  RadixSort.java   BucketSort.java
├── cpp/      counting_sort.cpp  radix_sort.cpp   bucket_sort.cpp
└── scheme/   counting_sort.scm  radix_sort.scm   bucket_sort.scm
```

## Running

Commands below are for counting sort; substitute the other file names to run
the rest.

**Python** (3.x):

```bash
python python/counting_sort.py
```

**Java** (JDK 8+) — compile, then run by class name:

```bash
cd java
javac CountingSort.java
java CountingSort
```

**C++** (any C++17 compiler):

```bash
cd cpp
g++ -std=c++17 -O2 counting_sort.cpp -o counting_sort
./counting_sort          # Windows: counting_sort.exe
```

**Scheme** (any R7RS interpreter; tested form below uses GNU Guile):

```bash
guile scheme/counting_sort.scm
# Chez Scheme:  scheme --script scheme/counting_sort.scm
```
