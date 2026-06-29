"""
quicksort.py
"""

import random


def _lomuto_partition(arr, low, high):
    """
    Partitions arr[low..high] around the pivot stored at arr[high].
    """
    pivot = arr[high]
    i = low - 1  # boundary of the "<= pivot" region

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low=0, high=None):
    """
    Sorts arr[low..high] in place using the last element as the pivot
    every time. This is the textbook deterministic Quicksort.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = _lomuto_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

    return arr


def randomized_quicksort(arr, low=0, high=None):
    """
    Sorts arr[low..high] in place. Identical to deterministic_quicksort,
    except the pivot is chosen uniformly at random from the current
    subarray before partitioning.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot_index = _lomuto_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

    return arr


if __name__ == "__main__":
    sample = [9, 4, 7, 1, 3, 8, 2, 6, 5]

    print("Original array:           ", sample)
    print("Deterministic quicksort:  ", deterministic_quicksort(sample.copy()))
    print("Randomized quicksort:     ", randomized_quicksort(sample.copy()))

    already_sorted = list(range(1, 11))
    print("\nAlready-sorted input:     ", already_sorted)
    print("Deterministic quicksort:  ", deterministic_quicksort(already_sorted.copy()))
    print("Randomized quicksort:     ", randomized_quicksort(already_sorted.copy()))
