# Algorithm Analysis

Companion code for the Module 01 (Algorithm Analysis) notes generated
by Claude (Opus 4.7). Each language implements the same set of
algorithms so students can see how the same asymptotic ideas
translate across very different paradigms.

Note that the Scheme and Prolog example use features of those 
languages that were not covered in CSC240.

## Contents

```(text)
csc310_module01/
├── python/algorithms_module01.py      ← all algorithms + empirical timing + race demo
├── java/AlgorithmsModule01.java       ← all algorithms + empirical timing
├── java/RaceConditionDemo.java        ← Java race-condition demo (Thread, synchronized, AtomicLong)
├── scheme/algorithms_module01.scm     ← recursive forms: search, sorts, Hanoi, factorial
└── prolog/algorithms_module01.pl      ← declarative forms: linear/binary search, sorts, Hanoi
```

## What each algorithm illustrates

| Algorithm                    | Big-Θ (worst)   | Big-Θ (best) | Space   | Lesson from the module |
|------------------------------|-----------------|--------------|---------|------------------------|
| Linear search                | Θ(n)            | Θ(1)         | Θ(1)    | upper bound vs. lucky inputs |
| Binary search                | Θ(log n)        | Θ(1)         | Θ(1)/Θ(log n) | assumption: sorted input |
| Insertion sort               | Θ(n²)           | Θ(n)         | Θ(1)    | CLRS Fig 2.1, loop analysis |
| Merge sort                   | Θ(n log n)      | Θ(n log n)   | Θ(n)    | divide & conquer, recurrences |
| Towers of Hanoi              | Θ(2ⁿ)           | Θ(2ⁿ)        | Θ(n)    | exponential blowup |
| Recursive factorial          | Θ(n)            | Θ(n)         | Θ(n)    | call-stack space cost |
| Iterative factorial          | Θ(n)            | Θ(n)         | Θ(1)    | iterative alternative |

## Running each

```bash
# Python (no install needed)
python3 algorithms_module01.py

# Java (JDK 11+)
javac *.java && java -ea AlgorithmsModule01
java RaceConditionDemo

# Scheme (Guile, Chicken, or any R7RS implementation)
guile  algorithms_module01.scm

# Prolog (SWI-Prolog)
swipl -q -t run_demos algorithms_module01.pl
```

## Why these four languages?

- **Python** — clean syntax, easy empirical timing, good threading
  primitives for the race-condition demo.
- **Java** — what CSC310 students are most likely using; explicit threading
  and `AtomicLong` make the race condition unambiguous; JIT/warmup gives a
  realistic look at performance measurement.
- **Scheme** — recursion is the natural style, which makes divide-and-conquer
  (merge sort, Hanoi) read like the math. Also shows tail recursion as the
  bridge between recursive and iterative — directly relevant to the
  "Recursive vs Iterative (Stack Space)" section of the notes.
- **Prolog** — Towers of Hanoi is a classic Prolog program; declarative
  insertion/merge sort show that the algorithmic structure is independent
  of paradigm; list membership maps to linear search.

## Where each ties back to the notes

- *Recursive vs Iterative Algorithms (Stack Space)* → `factorial_*` in all four files
- *Insertion Sort* (Example #3) → `insertion_sort` / `insertionSort` in Python, Java, Scheme, Prolog
- *Merge Sort* → `merge_sort` in all four files; the recurrence `T(n) = 2 T(n/2) + Θ(n)` is in the code comments
- *Towers of Hanoi* → `towers_of_hanoi` / `hanoi` in all four files; counts grow as `2ⁿ − 1`
- *Race Conditions* → `race_condition_demo` (Python), `RaceConditionDemo.java` (Java)
- *The Impact of Algorithm Choice* → empirical growth demo in Python and Java prints actual wall-clock ratios as `n` doubles
