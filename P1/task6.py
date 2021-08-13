"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    cur_head_1 = llist_1.head
    list_1 = []
    while cur_head_1:
        list_1.append(cur_head_1.value)
        cur_head_1 = cur_head_1.next
    
    cur_head_2 = llist_2.head
    list_2 = []
    while cur_head_2:
        list_2.append(cur_head_2.value)
        cur_head_2 = cur_head_2.next
    
    list_1.extend(list_2)
    result = sorted(set(list_1))
    return result


def intersection(llist_1, llist_2):
    # Your Solution Here
    cur_head_1 = llist_1.head
    list_1 = []
    while cur_head_1:
        list_1.append(cur_head_1.value)
        cur_head_1 = cur_head_1.next
    
    cur_head_2 = llist_2.head
    list_2 = []
    while cur_head_2:
        list_2.append(cur_head_2.value)
        cur_head_2 = cur_head_2.next
    
    result = list()

    for item in list_1:
        for it in list_2:
            if item == it:
                result.append(item)
                continue
    
    result = sorted(set(result))
    return result


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))  # [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]
print(intersection(linked_list_1, linked_list_2))  # [4, 6, 21]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  # [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]
print(intersection(linked_list_3, linked_list_4))  # []

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2,3,4,5]
element_2 = [5,6,7,8,9]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intersection(linked_list_5, linked_list_6))  # [5]

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [5,6,7,8,9]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))  # [5, 6, 7, 8, 9]
print(intersection(linked_list_7, linked_list_8))  # []

# Test case 5

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))  # []
print(intersection(linked_list_9, linked_list_10))  # []
