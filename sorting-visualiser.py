
import argparse
import random
from time import perf_counter


def merge_sort(arr, trace=False):
    """Return a sorted copy and the number of element comparisons."""
    comparisons = 0

    def sort(values):
        nonlocal comparisons

        if len(values) <= 1:
            return values[:]

        mid = len(values) // 2
        left = sort(values[:mid])
        right = sort(values[mid:])

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        if trace:
            print(f"Merge {left} + {right} -> {merged}")

        return merged

    return sort(arr), comparisons


def quick_sort(arr, randomized=False, trace=False):
    """Return a sorted copy and the number of pivot comparisons."""
    values = arr[:]
    comparisons = 0

    def sort(low, high):
        nonlocal comparisons

        if low >= high:
            return

        if randomized:
            pivot_index = random.randint(low, high)
            values[pivot_index], values[high] = (
                values[high], values[pivot_index]
            )

        pivot = values[high]
        boundary = low - 1

        for current in range(low, high):
            comparisons += 1

            if values[current] <= pivot:
                boundary += 1
                values[boundary], values[current] = (
                    values[current], values[boundary]
                )

        pivot_position = boundary + 1
        values[pivot_position], values[high] = (
            values[high], values[pivot_position]
        )

        if trace:
            print(
                f"Pivot {pivot}: {values[low:high + 1]} "
                f"(pivot index {pivot_position})"
            )

        sort(low, pivot_position - 1)
        sort(pivot_position + 1, high)

    sort(0, len(values) - 1)
    return values, comparisons


def bubble_sort(arr):
    """Return a sorted copy and the number of comparisons."""
    values = arr[:]
    comparisons = 0

    for end in range(len(values) - 1, 0, -1):
        swapped = False

        for i in range(end):
            comparisons += 1

            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True

        if not swapped:
            break

    return values, comparisons


def run_demo():
    data = [38, 12, 27, 43, 9, 31, 18, 25, 6, 14]

    print("Original array:", data)

    print("\n--- MERGE SORT ---")
    result, count = merge_sort(data, trace=True)
    print("Sorted:", result)
    print("Comparisons:", count)

    print("\n--- QUICK SORT (last-element pivot) ---")
    result, count = quick_sort(data, trace=True)
    print("Sorted:", result)
    print("Comparisons:", count)

    print("\n--- QUICK SORT (random pivot) ---")
    result, count = quick_sort(data, randomized=True, trace=True)
    print("Sorted:", result)
    print("Comparisons:", count)


def run_benchmark():
    print("\nCOMPARISON BENCHMARK")
    print("-" * 76)
    print(
        f"{'n':>6} {'Merge':>12} {'Quick':>12} "
        f"{'Random Q':>12} {'Bubble':>12}"
    )
    print("-" * 76)

    for n in (10, 100, 1000):
        data = [random.randint(0, 10000) for _ in range(n)]

        merge_result, merge_count = merge_sort(data)
        quick_result, quick_count = quick_sort(data)
        random_result, random_count = quick_sort(
            data, randomized=True
        )
        bubble_result, bubble_count = bubble_sort(data)

        assert merge_result == quick_result == random_result == bubble_result
        assert merge_result == sorted(data)

        print(
            f"{n:>6} {merge_count:>12} {quick_count:>12} "
            f"{random_count:>12} {bubble_count:>12}"
        )


def run_sorted_input_demo():
    # A sorted input exposes the weakness of a last-element pivot.
    # Use n=100 to keep this deliberately bad case manageable.
    data = list(range(100))

    _, first_count = quick_sort(data)
    _, random_count = quick_sort(data, randomized=True)

    print("\nSORTED INPUT: n = 100")
    print(f"Last-element pivot comparisons: {first_count}")
    print(f"Random-pivot comparisons:       {random_count}")


def main():
    parser = argparse.ArgumentParser(
        description="Terminal sorting visualiser and comparison benchmark"
    )
    parser.add_argument(
        "--mode",
        choices=("demo", "benchmark", "sorted", "all"),
        default="all",
        help="demo: show steps; benchmark: count comparisons; "
             "sorted: compare pivots on sorted input; all: run everything",
    )
    args = parser.parse_args()

    random.seed(42)

    if args.mode in ("demo", "all"):
        run_demo()

    if args.mode in ("benchmark", "all"):
        run_benchmark()

    if args.mode in ("sorted", "all"):
        run_sorted_input_demo()


if __name__ == "__main__":
    main()
