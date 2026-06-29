"""
benchmark.py

"""

import random
import sys
import time
import copy

from quicksort import deterministic_quicksort, randomized_quicksort

sys.setrecursionlimit(20000)


def make_random(n):
    return [random.randint(0, 1_000_000) for _ in range(n)]


def make_sorted(n):
    return list(range(n))


def make_reverse_sorted(n):
    return list(range(n, 0, -1))


def time_sort(sort_fn, data):
    """Runs sort_fn on a copy of data and returns elapsed seconds."""
    arr = copy.deepcopy(data)
    start = time.perf_counter()
    try:
        sort_fn(arr)
    except RecursionError:
        return None
    return time.perf_counter() - start


def run_trial(sort_fn, generator, n, trials=3):
    times = []
    for _ in range(trials):
        data = generator(n)
        t = time_sort(sort_fn, data)
        if t is None:
            return None
        times.append(t)
    return sum(times) / len(times)


def main():
    random_sizes = [1000, 5000, 10000, 20000]
    sorted_sizes = [500, 1000, 2000, 4000, 8000]  # smaller, deterministic hits O(n^2) here

    distributions = [
        ("Random", make_random, random_sizes),
        ("Sorted (ascending)", make_sorted, sorted_sizes),
        ("Reverse-sorted", make_reverse_sorted, sorted_sizes),
    ]

    results = []

    for label, generator, sizes in distributions:
        for n in sizes:
            det_time = run_trial(deterministic_quicksort, generator, n)
            rand_time = run_trial(randomized_quicksort, generator, n)
            results.append((label, n, det_time, rand_time))

    print(f"{'Distribution':<20}{'n':>8}{'Deterministic (s)':>20}{'Randomized (s)':>18}")
    print("-" * 66)
    for label, n, det_time, rand_time in results:
        det_str = f"{det_time:.5f}" if det_time is not None else "RecursionError"
        rand_str = f"{rand_time:.5f}" if rand_time is not None else "RecursionError"
        print(f"{label:<20}{n:>8}{det_str:>20}{rand_str:>18}")

    return results


if __name__ == "__main__":
    main()
