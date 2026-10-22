# Sorting Visualiser (Terminal)

**Project #5 of 100 | DSA in Practice**

A Python-based terminal application that demonstrates how Merge Sort, Quick Sort, and Bubble Sort work. It visualises sorting steps, counts element comparisons, and compares algorithm performance across different input sizes.

## Features

- **Merge Sort:** Displays the array after every merge operation.
- **Quick Sort:** Displays the pivot and array partition after every partition step.
- **Bubble Sort:** Provides a baseline for comparison counting.
- **Comparison Benchmark:** Compares algorithms on random arrays of 10, 100, and 1,000 elements.
- **Random Pivot:** Compares randomized Quick Sort with last-element-pivot Quick Sort on sorted input.
- **Correctness Checks:** Verifies that all sorting algorithms produce the expected sorted array.

## Technologies Used

- Python 3.10+
- Recursion
- Divide and conquer
- Lists and loops
- Random number generation
- Command-line arguments with `argparse`

No third-party packages are required.

## Project Structure

```text
week-02-sorting-visualiser/
├── sorting_visualiser.py
└── README.md
```

## Installation and Usage

### 1. Clone or download the repository

Open a terminal in the project directory.

### 2. Run the sorting demonstration

```bash
python sorting_visualiser.py --mode demo
```

Displays the original array, every Merge Sort merge step, and every Quick Sort partition step.

### 3. Run the comparison benchmark

```bash
python sorting_visualiser.py --mode benchmark
```

Prints comparison counts for array sizes of 10, 100, and 1,000 elements.

### 4. Compare pivot strategies

```bash
python sorting_visualiser.py --mode sorted
```

Compares last-element-pivot Quick Sort with randomized Quick Sort on an already sorted array.

### 5. Run all demonstrations

```bash
python sorting_visualiser.py --mode all
```

## Algorithm Comparison

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Bubble Sort | O(n)* | O(n²) | O(n²) |

*Bubble Sort achieves O(n) best-case time because it stops early when a complete pass