Search in a Rotated Sorted Array

In this case I used the binary search with some modifications since its complexity time is O(log(n)) as required by the problem.

Complexity in time:

In this case the while loop will run until the start index gets greater than the end index. Since each time of the loop the start or end index is divided by 2, the time complexity will be O(log(n)), so few elements will be checked at each loop, that are ordered at a certain point.

Complexity in space:

In this case the space used is O(1) since each variable space is reused and it is not a recursive function.
