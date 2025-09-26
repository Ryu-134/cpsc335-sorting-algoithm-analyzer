# generate input arrays and time the algorithms 
# encapsulate all timing logic here and keep algorithm files distinct


import random
import time


# function to create random list of numbers to sort
def generate_data(n, seed = None, condition="random"):      # defaults to random condition; conditions: random, sorted, reverse
    rng = random.Random(seed)               # create random seed OR is deterministic if a seed is provided
    values = [] 
    high = max(10, n * 10)      # widen value range as n grows
    for _ in range(n):
        values.append(rng.randint(-high, high))

    if condition == "random":
        return values
    elif condition == "sorted":
        return sorted(values)
    elif condition == "reverse":
        return sorted(values, reverse=True)
            

# function to time algorithms
def time_algorithms(function, data):
    arr = data[:]       # each algorithm MUST get identical input for accurate analysis --> create shallow copy via slicing with arr[:]
    start = time.perf_counter()
    function(arr)   # sort IN-PLACE and ignore return; ONLY care about time it takes to sort
    end = time.perf_counter()
    elapsed = end - start
    return elapsed    
