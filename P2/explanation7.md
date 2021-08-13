HTTPRouter using a Trie

In this case the Trie structure is the most appropriate due its facilitation to save nodes and its children forming a pattern, that in this case will be formed by the path and its subpath sequences.

Complexity in time:

In this case the worst case scenario is in the functions that requires to do a transversal in the trie. The insert method on the Trie will look for all the subpaths that are part of the path. If the path was already on the trie or it is just missing one part to save, the complexity will be O(n).

For the find function we have that it seeks for the subpaths sequentially in the node and in its children. After finally finding all the subpaths, it will check if the leaf node has a viable handler or will return the default error handler. This implies that it will run for all the parts of the input, implying a time complexity of O(n).

Since each function gives the same time complexity, the worst case scenario here is O(n).

Complexity in space:

In this case, the trie saves each subpath and sequences between them to form paths. Each subpath has a dictionary of nodes that are its children (each subpath of the path), and a handler variable. This implies a space complexity of O(path * subpaths).
