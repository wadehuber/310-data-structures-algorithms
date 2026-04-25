# String Algorithms

## Contents

- [Videos](#videos)
- [KMP Pattern Matcher](#kmp-pattern-matcher)
- [Rabin-Karp Rolling Hash](#rabin-karp-rolling-hash)
- [Suffix Array with LCP](#suffix-array-with-lcp)
- [Complexity Analysis](#complexity-analysis)

## Videos

[Naive & KMP Algorithm](https://www.youtube.com/watch?v=ynv7bbcSLKE)
[MIT Lecture on Karp-Rabin](https://youtu.be/BRO7mVIFt08?si=AnlbddLAszRvPt8D)

---

## KMP Pattern Matcher

**File:** `kmp_matcher.py`

The Knuth-Morris-Pratt algorithm finds all occurrences of a pattern in text by using a prefix function (failure function) to avoid redundant character comparisons.

---

## Rabin-Karp Rolling Hash

**File:** `rabin_karp_matcher.py`

The Rabin-Karp algorithm uses polynomial rolling hashes to quickly find pattern matches. It's particularly effective for multiple pattern matching and is the basis for many string processing techniques.

## Suffix Array with LCP

**File:** `suffix_array.py`

A suffix array is a sorted array of all suffixes of a text. The LCP (Longest Common Prefix) array stores the length of the longest common prefix between consecutive suffixes. Together, they enable efficient pattern matching, substring queries, and other string operations.

---

## Complexity Analysis

| Algorithm | Pattern Matching Time | Space | Best For |
|-----------|---------------------|-------|----------|
| **KMP** | O(n + m) | O(m) | Single pattern, guaranteed linear time |
| **Rabin-Karp** | O(n + m) avg | O(1) | Multiple patterns, hashing-based use cases |
| **Suffix Array** | O(n² log n) build | O(n) | Substring queries, repeated patterns, LCP queries |

Where:

- `n` = text length
- `m` = pattern length
