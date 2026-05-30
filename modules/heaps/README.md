# Heaps & Priority Queues

## Ports of the Java implementation

The original code in this repo is Java. The `python/`, `cpp/`, and
`prolog/` directories re-implement it in other languages.

- **`python/`** — a near line-for-line port of the Java linked-tree
  `LinkedHeap` and `PriorityQueue`. Same class/method structure, one file
  per Java file. Run the demos:
  ```
  python python/heap_example.py
  python python/pq_tester.py
  ```
- **`cpp/`** — the same 1-1 port using header-only templates (`this->`
  is required to reach inherited members in template subclasses). Build:
  ```
  g++ -std=c++17 cpp/PQTester.cpp    -o PQTester    && ./PQTester
  g++ -std=c++17 cpp/HeapExample.cpp -o HeapExample && ./HeapExample
  ```
- **`prolog/`** — a *functional* heap. Prolog has no mutable state, so
  instead of rewiring tree nodes in place it uses a persistent **leftist
  min-heap** where every operation is built on `merge/3`. Run:
  ```
  swipl -q -g main -t halt prolog/demo.pl
  ```

All three reproduce the Java `PQTester` output (lower priority first,
ties broken first-come-first-served).

## Bonus: heap construction complexity

[`heapify_complexity.py`](heapify_complexity.py) is a standalone, self-contained
demo (it does not import the port above) that explains why building a heap by
**naive insertion is O(n log n)** but **bottom-up heapify is O(n)**. It uses a
small swap-counting min-heap to:

- trace `heapify` on a tiny array,
- run an experiment that prints *swaps per element* as `n` grows — the naive
  column keeps climbing (the log factor) while heapify stays flat below 1
  (linear), and
- walk through the `sum(h / 2^h) = 2` argument for why the log factor collapses.

Run it:
```
python heapify_complexity.py
```

## heaps

[Video: Overview of Heaps & Priority Queues](https://youtu.be/cRzgDdtvgCI) (7:24)

### Implementing Heaps in Java

  - Video 1 of 3: [Introduction to min & max heaps, HeapNode, & LinkedHeap](https://youtu.be/sj6QqonekkY) (7:55)
  - Video 2 of 3: [Adding elements to a min heap](https://youtu.be/D4ywzZn2jo0) (10:07)
  - Video 3 of 3: [Removing elements from a min heap](https://youtu.be/z3tFZVaJTGQ) (9:11)

### Code

Code walk through in Eclipse - these videos cover all the code from the package, so there is some overlap with the Implementing Heaps videos.

  - [Video 1 - Using heaps, HeapADT interface, HeapNode class, Linked Heap class, adding elements](https://youtu.be/gypH36ka7Ls) (11:28)
  - [Video 2 - Removing elements from a min heap - removeMin()](https://youtu.be/MIIyYW2I2dI) (7:00)

### Utility classes (used for examples)

- HeapExample.java - example of using a Heap
- StudentRecord.java - class we will add to a Heap
- SortPhoneList - example of using heapSort
- Contact.java - class we will sort using HeapSort

### csc205

[Video - HeapSort](https://youtu.be/p9SA1cD5GW8) (1:36)

- Sorting.java - Sorting class that includes heapSort

### priorityqueue

Videos:

- [Overview of Priority Queues & the Prioritized Object class](https://youtu.be/4OULGDYpzJI) (10:06)
- [Code walk through](https://youtu.be/H_eCyBqLlGQ) (5:44)

Code:

- PriorityQueue.java - Implementation of a Priority Queue using a Heap
- PrioritizedObject.java - Helper object for use in a Priority Queue
- PQTester.java - Priority Queue test driver class
