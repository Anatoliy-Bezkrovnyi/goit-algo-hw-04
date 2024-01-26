import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

if __name__ == "__main__":
    data_small = [random.randint(0, 1000) for _ in range(1000)]
    data_medium = [random.randint(0, 10000) for _ in range(10000)]

    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=10)

    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=10)

    print(f"{'|Algorythm': <20} | {'Time small data' : <20} | {'Time medium  data' : <20}")
    print(f"{'-'*20} | {'-'*20} | {'-'*20}")
    print(f"{'|Insertion sort': <20} | {time_small_insertion : <20.5f} | {time_medium_insertion : <20.5f}")
    print(f"{'|Merge sort': <20} | {time_small_merge : <20.5f} | {time_medium_merge : <20.5f}")
    print(f"{'|Timsort': <20} | {time_small_timsort : <20.5f} | {time_medium_timsort : <20.5f}")