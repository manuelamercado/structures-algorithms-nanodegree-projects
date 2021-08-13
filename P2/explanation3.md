Search in a Rotated Sorted Array

In this case I used the merge sort (sorting elements descendent order) since its complexity time is O(n log(n)) as required by the problem.

Complexity in time:

In this case the merge function time complexity is O(n). Since it is called by the mergesort function, that is dividing the elements recursively, its time complexity is O(log(n)), and then multiply this by the merge function, the time complexity will be O(n log(n)). For the rearrange_digits function the time complexity is O(n). Sum all of these and time complexity will be O(n log(n)) + O(n). The worst case scenario here is O(n log(n)), so this is the answer.

Complexity in space:

In this case the space used by the merge sort functions is similar to its time complexity, since mergesort function is recursive and is calling merge function. The first one store elements dividing the list by 2 in each call, and merge function is storing all elements in a list with the same length as its input. The rearrange_digits function store the elements in arrays with the same length as its input. In conclusion, the worst case scenario here is O(n log(n)).
