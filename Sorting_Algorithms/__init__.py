# python package to bring in and run all algorithms at once to time them at once

from .Counting_Sort import counting_sort
from .Heap_Sort import heap_sort
from .Quick_Sort import quick_sort
# import remaining algorithms




ALGORITHMS = {
    "Counting": counting_sort,
    "Heap": heap_sort,
    "Quick": quick_sort    
    # fill in remaining algorithms
}


