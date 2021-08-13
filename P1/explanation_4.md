Active Directory

In this case we are using a Group class, with some arrays for storing the data. This allows object instances to have groups, and subgroups, stored in the arrays as references.

Complexity in time

In this case the most consuming operation is the function to determine if an user is in a group. This will depends on the depth of the groups. Then we have to iterate in users arrays to check if user exists there. In conclusion, time complexity will be O(depth x users).

Complexity in space

In this case we have arrays of users that are variables in size, and groups with subgroups. In conclusion, we need a space of O(depth * users).
