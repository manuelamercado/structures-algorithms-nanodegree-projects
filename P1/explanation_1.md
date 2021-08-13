LRU Cache

In this case I used a class for managing the principal part,
with a double linked list for inserting and deleting in a quicker time, and a dictionary for managing the cache, since this allow insertion and get requests in O(1).

Complexity in time:

Insertion in general requires O(1) complexity, considering the worst case scenario, since in each structure and operation is the same time of O(1). This is the same required for getting a value.

Insertion:
- If cache is not full:
In dict O(1), in list O(1)
- If cache is full it requires a delete operation in dict that is O(1), and a remove in list that is O(1) since we delete the tail and we know its location.

Get
The get in the dict is 0(1). Since we use this value (node) for pre-appending the data and deleting, we got the same time complexity of O(1).

Complexity in space:

The cache requires an space on O(n) in case it gets full. This is the same case with the list. This will be O(n) + O(n), that is O(2n), but considering the worst case scenario the complexity in space is O(n) since O(2n) is a linear function as well.
