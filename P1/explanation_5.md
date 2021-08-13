Blockchain

In this case we are using Block class that is a node for the BlockChain that is a linked list. The Block class has a method to calculate the hash using the data (this one was provided). Using these structures the blockchain problem can be emulated, since each block has the hash from the previous node and it needs to save its proper data.

Complexity in time:

For inserting a new node, that is always at the head, we have O(1) in complexity. The only method that is O(n) is the to_list method and is optional, for debugging purposes. I would say that time complexity here is O(1).

Complexity in space

The space we need is the same space of the input, for saving them in the nodes from the linked list. The worst case here is O(n).
