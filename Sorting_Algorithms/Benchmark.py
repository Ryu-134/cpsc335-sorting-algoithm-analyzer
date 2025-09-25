# class to generate random numbers and run timer to benchmark all algorithms
# wanted to encapsulate all timing logic here and keep algorithm files distinct
import random
import time
from . import ALGORITHMS


# function to create random list of numbers to sort
def generate_data(input, seed = None):      # have user decide # of random #'s to generate and have seed parameter to possibly input same seed to test
    rng = random.Random(seed)               # create random seed
    values = [] 
    high = max(10, input * 10)
    for val in range(input):
        values.append(rng.randint(0, high))
    return values 


# function to time algorithms
def time_algorithms(function, data):
    arr = data[:]
    start = time.perf_counter()
    function(arr)
    end = time.perf_counter()
    elapsed = end - start
    return elapsed    
