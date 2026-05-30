# Quicksort

Quicksort is a divide-and-conquer sorting algorithm:

1. **Partition** — pick a *pivot* element and rearrange the data so everything
   less than the pivot comes before it and everything greater comes after it.
   The pivot is now in its final sorted position.
2. **Recurse** — quicksort the partition to the left of the pivot and the
   partition to the right of it.

Average-case running time is **O(n log n)**; the worst case is **O(n²)** when
the pivot consistently splits the data badly (see the pivot demo below).

Videos:

- [VIDEO: Merge Sort & Quicksort](https://youtu.be/U_xq6UnJ2Ks) (15:59)
- [VIDEO: Quicksort overview & Java code walk through](https://youtu.be/-2w5LPqP8Gs) (9:58)

## Implementations

The same quicksort is implemented in several languages. The array-based ports
(Java, C++, Go) use the **middle element** as the pivot and partition in place,
matching the original Java version. The list-based ports (Scheme, Prolog) use
the classic *functional / declarative* formulation, which builds new sublists
instead of mutating an array. Each file includes a small test harness that
sorts random data and verifies the result.

| Language | File | Style | How to run |
|----------|------|-------|------------|
| Java   | [QuickSort.java](QuickSort.java)     | in-place array, middle pivot | `javac QuickSort.java && java quicksort.QuickSort` |
| C++    | [QuickSort.cpp](QuickSort.cpp)       | in-place vector, middle pivot | `g++ -std=c++17 -O2 -o QuickSort QuickSort.cpp && ./QuickSort` |
| Python | [quick_sort.py](quick_sort.py)       | in-place list, middle pivot | `python quick_sort.py` |
| Go     | [quicksort.go](quicksort.go)         | in-place slice, middle pivot | `go run quicksort.go` |
| Scheme | [quicksort.scm](quicksort.scm)       | functional, list-based | `guile quicksort.scm` |
| Prolog | [quicksort.pl](quicksort.pl)         | declarative, list-based | `swipl quicksort.pl` |

> The Java source lives in a `quicksort` package, so run it with the package
> name: `java quicksort.QuickSort`.

## Choosing a pivot matters: [pivot_comparison.py](pivot_comparison.py)

Quicksort's speed depends almost entirely on how evenly each partition splits
the data, and that is decided by the pivot. This script implements quicksort
once, parameterized by a *pivot strategy*, counts the comparisons each strategy
makes, and runs them all against several input shapes (random, already sorted,
reverse sorted, all equal).

Strategies compared:

- **first element**
- **last element**
- **middle element**
- **random element**
- **median of three** (median of the first, middle, and last elements)

Run it:

```(bash)
python pivot_comparison.py
```

Sample output (`n = 500`; lower comparison counts are better):

```(text)
pivot strategy           random  already sorted  reverse sorted       all equal
-------------------------------------------------------------------------------
first element             7,479         125,747         125,498         125,249
last element              6,567         125,249         125,498         125,249
middle element            6,926           4,124           4,918         125,249
random element            6,899           5,686           5,725         125,249
median of three           6,271           4,124          32,621         125,249
```

What to notice:

- **first / last** explode to the O(n²) worst case on sorted and
    reverse-sorted data — exactly the inputs they are most likely to meet in
    practice — and the deep recursion can even overflow the stack.
- **middle** dodges those particular adversaries, but inputs can still be
    constructed to defeat it.
- **random** and **median of three** stay near the O(n log n) target across
    every shape, which is why real-world libraries use strategies like these.
- **all equal** is the worst case for *every* strategy: no pivot choice helps
    when all keys are identical. Fixing that needs three-way ("Dutch national
    flag") partitioning, which groups equal keys together in the middle.

## Attribution

The implementations are adapted from the code provided with:

- *Java Foundations* (2nd & 3rd ed.) by Lewis, DePasquale, & Chase
- *Algorithms* (4th ed.) by Sedgewick & Wayne

Python, C++, Prolog, Go, & Scheme implementations created by Claude Code (Opus 4.8)
