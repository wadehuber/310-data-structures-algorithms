"""
Offline Caching: Belady's MIN vs. LRU  (CSC310 Module 12 - Greedy Algorithms)
============================================================================

The OFFLINE caching problem knows the whole request sequence in advance.  The
greedy rule "on a miss with a full cache, evict the item whose next use is
farthest in the future" (Belady's MIN) is provably optimal -- it causes the
fewest possible misses.  An ONLINE policy like LRU cannot see the future, so it
generally suffers more misses.  This program runs both on the same input and
prints a miss-by-miss trace so you can see why MIN wins.
"""
from typing import List


def belady(requests: List[int], k: int):
    """Optimal offline policy: evict the page whose next use is farthest away."""
    cache, misses, trace = [], 0, []
    for t, page in enumerate(requests):
        if page in cache:
            trace.append((page, "hit", list(cache)))
            continue
        misses += 1
        if len(cache) < k:
            cache.append(page)
            trace.append((page, "miss/load", list(cache)))
        else:
            # choose the cached page used farthest in the future (or never)
            def next_use(p):
                for j in range(t + 1, len(requests)):
                    if requests[j] == p:
                        return j
                return float("inf")
            victim = max(cache, key=next_use)
            cache[cache.index(victim)] = page
            trace.append((page, f"miss/evict {victim}", list(cache)))
    return misses, trace


def lru(requests: List[int], k: int):
    """Online policy: evict the least-recently-used page."""
    cache, misses, trace = [], 0, []   # cache ordered oldest-use -> newest-use
    for page in requests:
        if page in cache:
            cache.remove(page)
            cache.append(page)
            trace.append((page, "hit", list(cache)))
            continue
        misses += 1
        if len(cache) < k:
            cache.append(page)
            trace.append((page, "miss/load", list(cache)))
        else:
            victim = cache.pop(0)
            cache.append(page)
            trace.append((page, f"miss/evict {victim}", list(cache)))
    return misses, trace


def show(name, misses, trace):
    print(f"=== {name}: {misses} misses ===")
    for page, action, cache in trace:
        print(f"  request {page:<2}  {action:<14}  cache={cache}")
    print()


def main():
    requests = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    k = 3
    print(f"Request sequence: {requests}")
    print(f"Cache size k = {k}\n")

    bm, bt = belady(requests, k)
    lm, lt = lru(requests, k)
    show("Belady's MIN (optimal, offline)", bm, bt)
    show("LRU (online)", lm, lt)

    print(f"Belady misses = {bm}, LRU misses = {lm}")
    print("Belady is optimal, so it never has more misses than LRU.")


if __name__ == "__main__":
    main()
