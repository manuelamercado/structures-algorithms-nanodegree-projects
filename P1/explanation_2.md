Finding Files

In this case I used a recursive function due the form of the problem, checking the same things up and down. Here I used the recommended functions for checking the files.

Complexity in time:

In this case the recursive function will be run for each directory and subdirectories, that are nodes, that could be like tranversing a tree, which time is O(n).

Complexity in space:

In this case the recursion function will be using a space that depends on the depth in the worst case, so it will be O(depth). If considering the result array it will be less than O(n), so it will be O(s). Finally space complexity will be O(s + depth).
