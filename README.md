# Sorting Algorithms Project

This repository implements and analyzes classical sorting algorithms as part of **CSUF Group Project #1**. 
The project includes both benchmarking code (for performance comparison) and visualization code (for demonstration purposes).

---

## Repository Structure

### 1. `Sorting_Algorithms/`

* Contains pure algorithm implementations (e.g., Bubble Sort, Quick Sort, Merge Sort, Counting Sort, etc.).
* These versions are **optimized for benchmarking only** — they avoid visualization overhead to ensure accurate performance measurements.

### 2. `algo_visualization/`

* Contains sorting algorithms adapted for **visualization demos**.
* Includes logic for animating the sorting process using matplotlib.
* Supports **keyboard navigation** to step through and observe how each algorithm operates in real-time.

### 3. `plot.py`

* A standalone script that runs **all algorithms at once** on benchmark data.
* Generates comparison-style plots using matplotlib to visually compare the relative performance of algorithms.

---

## Benchmark Data

The raw timing data (across multiple trials, input sizes, and data conditions) is stored in a Google Sheet:

👉 [View the Benchmark Results Here](https://docs.google.com/spreadsheets/d/1zFAZfrti3uUUGHU31yiro4l6Kk82yEmsEZV4Mqlnnd0/edit?gid=0#gid=0)

This dataset includes results for input sizes of **100, 1000, and 10000** under three data conditions:

* **Random** (random integers, including negatives)
* **Sorted** (ascending order input)
* **Reverse** (descending order input)


### Key Takeaways

* **Quadratic algorithms (Bubble, Insertion)** confirm theory: fine on small inputs but quickly become impractical for larger datasets.
* **Divide-and-conquer algorithms (Quick, Merge, Heap)** scale predictably with O(n log n) growth and perform well up to N=10,000.
* **Linear-time algorithms (Counting, Bucket, Radix)** are the most efficient for large inputs, though they rely on integer-based assumptions or uniform distribution.
* **Quick Select** efficiently handles selection problems (like finding medians) without needing to sort the entire dataset.

---

## Usage

* Run benchmarks (no visualization):

  ```bash
  python main.py
  ```

* Run algorithm visualizations:

  ```bash
  python algo_visualization/main.py
  ```

* Generate performance comparison plot:

  ```bash
  python plot.py
  ```

---

## Notes

* Benchmarking was done under multiple data conditions: **random, sorted, reverse**.
* Visualization is intended for educational/demo purposes and is not optimized for runtime performance.
* All algorithms were implemented **in-place** for consistency with benchmarking logic.

