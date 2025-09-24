# CLI -based test file for algos before going to GUI

from Sorting_Algorithms import ALGORITHMS           
from Benchmark import generate_data, time_algorithms

def main():
    try:
        n_text = input("How many random numbers to generate? ").strip()
        n = int(n_text)
        if n <= 0:
            raise ValueError
    except Exception:
        print("Please enter a positive integer for N.")
        return

    data = generate_data(n, seed=42)    # generate data ONCE so all algorithms work off same input

    wanted = ["Counting", "Heap", "Quick"]      # update as we add more sorting algorithms
    algos = {name: ALGORITHMS[name] for name in wanted if name in ALGORITHMS}

    if not algos:
        print("No matching algorithms found in your registry.")
        return

    print("\nTiming algorithms on n={}, random data:\n".format(n))

    # Time and print
    for name, fn in algos.items():
        secs = time_algorithms(fn, data)
        print("{:<10}  {:.6f} sec".format(name, secs))

if __name__ == "__main__":
    main()
