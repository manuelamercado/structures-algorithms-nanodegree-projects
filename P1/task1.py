"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""


class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def preappend(self, key, value, node=None):
        head = self.head

        if node == head and node is not None and head is not None:
            return

        if node is None:
            node = DoubleNode(key, value)
        else:
            self.remove(node)

        node.next = head
        node.previous = None
        self.head = node

        if self.tail is None:
            self.tail = self.head

        if head is not None:
            head.previous = self.head

        return self.head

    def remove(self, node):
        if self.head is None:
            return

        if node == self.tail:
            node.previous.next = None
            self.tail = node.previous
        elif node == self.head:
            node.next.previous = None
            self.head = node.next
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


class LRU_Cache(object):
    def __init__(self, capacity=5):
        # Initialize class variables
        self.list = DoublyLinkedList()
        self.bucket = dict({})
        self.num_entries = 0
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            if self.bucket[key] is not None:
                self.list.preappend(key, None, self.bucket[key])
                return self.bucket[key].value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == 0:
            return
        if self.list.head is None or self.num_entries < self.capacity:
            self.bucket[key] = self.list.preappend(key, value)
            self.num_entries += 1
        else:
            del self.bucket[self.list.tail.key]
            self.list.remove(self.list.tail)
            self.bucket[key] = self.list.preappend(key, value)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#Edge cases
#Capacity 0
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
result = our_cache.get(1)  # returns -1 because the cache has no capacity
print(result)
#Capacity 10 High Capacity
our_cache = LRU_Cache(10)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # returns 3
print(our_cache.get(4))  # returns 4
our_cache.set(7, 7)
print(our_cache.get(5))  # returns 5
result = our_cache.get(6)  # returns 6
print(result)
