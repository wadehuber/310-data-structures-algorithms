# Medians & Order Statistics

Runnable examples that complement the **Module 03B — Medians & Order
Statistics** notes. The selection problem asks for the i-th smallest element
(the median is the special case i ≈ n/2). Unlike full sorting, selection only
needs one element, so it can beat the Ω(n log n) sorting bound. These examples
demonstrate the selection algorithms and the robustness property of the median.

These are illustrations of the concepts only — they are **not** solutions to the
lab or homework questions.

Every example is provided in four languages. They implement the same algorithm
the same way and print the same output, so you can read whichever language you
are most comfortable with.

## Examples

| Topic | Demonstrates | Python | Java | C++ | Scheme |
|-------|--------------|--------|------|-----|--------|
| RANDOMIZED-SELECT (quickselect), Θ(n) expected | Selecting the i-th smallest with a random pivot and partition, recursing into only one side | [`randselect.py`](python/randselect.py) | [`RandSelect.java`](java/RandSelect.java) | [`randselect.cpp`](cpp/randselect.cpp) | [`randselect.scm`](scheme/randselect.scm) |
| Median-of-medians SELECT, O(n) worst case | The deterministic "groups of 5" pivot that guarantees linear time, verified against every rank | [`select_medians.py`](python/select_medians.py) | [`SelectMedians.java`](java/SelectMedians.java) | [`select_medians.cpp`](cpp/select_medians.cpp) | [`select_medians.scm`](scheme/select_medians.scm) |
| Robust statistics | How a single outlier drags the mean but leaves the median nearly fixed | [`mean_median.py`](python/mean_median.py) | [`MeanMedian.java`](java/MeanMedian.java) | [`mean_median.cpp`](cpp/mean_median.cpp) | [`mean_median.scm`](scheme/mean_median.scm) |

`randselect` and `select_medians` solve the *same* problem two ways: the
randomized version is simple and fast in practice, while median-of-medians trades
larger constants for a worst-case guarantee — a classic theory-vs-practice
contrast called out in the notes.

## Directory layout

```text
statistics/
├── python/   randselect.py    select_medians.py    mean_median.py
├── java/     RandSelect.java  SelectMedians.java   MeanMedian.java
├── cpp/      randselect.cpp   select_medians.cpp   mean_median.cpp
└── scheme/   randselect.scm   select_medians.scm   mean_median.scm
```

## Running

Commands below are for `randselect`; substitute the other file names to run
the rest.

**Python** (3.x):

```bash
python python/randselect.py
```

**Java** (JDK 8+) — compile, then run by class name:

```bash
cd java
javac RandSelect.java
java RandSelect
```

**C++** (any C++17 compiler):

```bash
cd cpp
g++ -std=c++17 -O2 randselect.cpp -o randselect
./randselect             # Windows: randselect.exe
```

**Scheme** (any R7RS interpreter; tested form below uses GNU Guile):

```bash
guile scheme/randselect.scm
```
