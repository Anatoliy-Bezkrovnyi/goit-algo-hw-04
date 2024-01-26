## Sorting algorithms comparison

**Sorting algorithms selected for comparison:**

 - Insertion sort
 - Merge sort
 - Timsort (inbuild Python sorting algorithm)

**Test strategy:** 
Measuring the time needed to sort given set of values. Two testing data sets were prepared: unsorted arrays with 1000 and 10 000 elements inside. Both arrays were sorted by selected algorithms one by one.

**Test results:** 
| Algorithm| Small Data Time| Large Data Time|
| ------ | ---------- | ---------- |
|**Insertion sort**|0.22589 | 27.48791
|**Merge sort**|0.02175 |0.31117
|**Timsort**|0.00109 |0.02061

**Conclusions:**
As can be seen from the provided testing results, all algorithms have shown acceptable time of work on small amounts of data. However, even on small amounts **Timsort** algorithm hundred times faster then its opponents. Everything become even worse on large amount of data: **Insertion sort** took 27 seconds to solve the task while 0.02 is enough for **Timsort**. Testing proves that inbuild Python sorting algorithm is the most balanced and the fastest algorithm from the list of available.