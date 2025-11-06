

import random
import time
import heapq

# ------------------ HEAPSORT IMPLEMENTATION ------------------ #
def heapify(arr, n, i):
    """Maintains max-heap property for subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Compare right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    """Sorts an array using Heapsort (max-heap)."""
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move max to end
        heapify(arr, i, 0)
    return arr


# ------------------ COMPARISON WITH OTHER SORTS ------------------ #
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def compare_sorts():
    """Compares Heapsort, Quicksort, and Merge Sort performance."""
    sizes = [1000, 5000, 10000]
    distributions = {
        "Random": lambda n: [random.randint(0, 10000) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
    }

    print("\n--- Sorting Algorithm Comparison ---")
    for dist_name, generator in distributions.items():
        print(f"\nInput Distribution: {dist_name}")
        for n in sizes:
            data = generator(n)

            for name, func in [
                ("Heapsort", lambda a: heapsort(a.copy())),
                ("Quicksort", lambda a: quicksort(a.copy())),
                ("Merge Sort", lambda a: mergesort(a.copy())),
            ]:
                start = time.time()
                func(data)
                elapsed = time.time() - start
                print(f"{name:<10} | n={n:<6} | Time: {elapsed:.5f}s")
        print("-" * 50)


if __name__ == "__main__":
    compare_sorts()



