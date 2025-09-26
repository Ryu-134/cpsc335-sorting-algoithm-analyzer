import matplotlib.pyplot as plt
import numpy as np
import random
import time
from Sorting_Algorithms import ALGORITHMS

def generate_data(input, seed=None):
# Generate random amt of numbers to be sorted
    rng = random.Random(seed)
    values = []
    high = max(10, input * 10)
    for _ in range(input):
        values.append(rng.randint(0, high))
    return values

def time_algorithms(function, data):
# times algorithm run time
    arr = data[:]
    start = time.perf_counter()
    function(arr)
    end = time.perf_counter()
    elapsed = end - start
    return elapsed

def create_plot(algorithm_results):
# creates plot using numpy and matplotlib
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    for name, results in algorithm_results.items():
        n_elements = [r[0] for r in results]
        elapsed_times = [r[1] for r in results]
        ax.plot(n_elements, elapsed_times, marker='o', linestyle='-', label=name)

    ax.set_xlabel('Number of Elements (n)', fontsize=14)
    ax.set_ylabel('Time (seconds)', fontsize=14)
    ax.set_title('Performance of Sorting Algorithms by Input Size', fontsize=16)
    ax.legend(loc='upper left', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    plt.show()

def main():
# run benchmark
    print("Running benchmarks...")
    
    input_sizes = [1000, 5000, 10000]
    
    algorithm_results = {name: [] for name in ALGORITHMS.keys()}

    for n in input_sizes:
        data = generate_data(n, seed=42)
        print(f"\nTiming algorithms on n={n}, random data:")
        for name, func in ALGORITHMS.items():
            elapsed = time_algorithms(func, data)
            print(f"{name:<10}  {elapsed:.6f} sec")
            algorithm_results[name].append((n, elapsed))

    create_plot(algorithm_results)

if __name__ == '__main__':
    main()
