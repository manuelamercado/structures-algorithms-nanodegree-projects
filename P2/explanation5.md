Building a Trie in Python

In this case the Trie structure is the most appropriate due its facilitation to save nodes and its children forming a pattern, that in this case will be formed by the words and its letter sequences.

Complexity in time:

In this case the worst case scenario is in the functions that requires to do a transversal in the trie. The insert method on the Trie will look for all the letters that are part of the word. If the word was already on the trie or it is just missing one letter to save, the complexity will be O(n).

For the find function we have that it seeks for the letters sequentially in the node and in its children. After finally finding some word (is_word), it continues searching at the next children of the final letter of the prefix (node) to form the array with all the suggestions. This implies a time complexity of O(words * letters). This is the worst case scenario.

Complexity in space:

In this case, the trie saves each letter and sequences between them to form words. Each letter has a dictionary of nodes that are its children (each letter of the word), and a boolean variable called is_word. This implies a space complexity of O(words * letters).
