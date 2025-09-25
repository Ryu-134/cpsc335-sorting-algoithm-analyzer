# python package to bring in and run all algorithms at once to time them at once

from .Counting_Sort import counting_sort
from .Heap_Sort import heap_sort
from .Quick_Sort import quick_sort
from .Bubble_Sort import bubble_sort
from .Insertion_sort import insertion_sort
from .Merge_Sort import merge_sort
from .Bucket_Sort import bucket_sort
from .Radix_Sort import radix_sort_lsd
from .Quick_Select import timed_quick_select


# import remaining algorithms




ALGORITHMS = {
    "Counting": counting_sort,
    "Heap": heap_sort,
    "Quick": quick_sort,
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Bucket": bucket_sort,
    "Radix": radix_sort_lsd,
    "Select": timed_quick_select
}
