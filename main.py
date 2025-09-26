# Benchmark Runner: generates data under VARYING conditions and times each algorithm 
# Data conditions 
# 1) random: randomly generated ints (includes negatives)
# 2) sorted: same randomly generated ints in ascending order
# 3) reverse: same randomly generated ints in descending order

from Sorting_Algorithms import Benchmark, ALGORITHMS

def main():
    print("Running benchmarks...")
    N = 10000   # number of elements to generate; adjust as needed --> currently testing 100, 1000, 10000
    SEED = 42   # DANGER: keep a set seed to allow for reproducible runs during testing for accurate analysis
    CONDITIONS = ["random", "sorted", "reverse"]    
    
    for condition in CONDITIONS:
        data = Benchmark.generate_data(N, seed=SEED, condition=condition)
        print(f"\nCondition: {condition}, n={N}")
        for name, func in ALGORITHMS.items():
            elapsed = Benchmark.time_algorithms(func, data)
            print(f"{name:<12} {elapsed:.6f} seconds")
    
if __name__ == "__main__":
    main()
    