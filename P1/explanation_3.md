Data Compression

In this case I used a Tree class with a Node class for storing the characters and its binary values, as described in the problem. I selected an array for managing the nodes and a sorted statement because we get always the smallest nodes and with this structure it will be easier to implement and to get the values, also for inserting the parent node in each iteration. I used recursion functions to tranverse the structure of the tree (with levels).

Complexity in time

- Encoding:
For encoding, the data we have some complete iterations that depends on the input size, so for those cases the complexity is O(n). The other operations like inserting the nodes array and in the tree (the root node) are just O(1), so worst case scenario here is O(n).

- Decoding:
For decoding we have to iterate all over the input size, that is O(n), that is the same time complexity for iterating through the tree, so worst case scenario here is O(n).

Complexity in space

We store the data in a dictionary and in a tree, and in some auxiliary arrays, that are O(n). Since they required the same space, worst case scenario here is O(n).
