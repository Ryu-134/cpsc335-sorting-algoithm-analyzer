from Sorting_Algorithms import Benchmark, ALGORITHMS

def main():
    print("Running benchmarks...")
    data = Benchmark.generate_data(10000) # generate 10,000 elements to sort
    for name, func in ALGORITHMS.items():
        elapsed = Benchmark.time_algorithms(func, data)
        print(f"{name} sort took {elapsed:.6f} seconds")

if __name__ == "__main__":
    main()