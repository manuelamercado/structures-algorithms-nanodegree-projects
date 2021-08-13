import random

'''
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?
'''


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return (None, None)

    min = ints[0]
    max = ints[0]

    for num in ints:
        if num < min:
            min = num
            continue

        if num > max:
            max = num

    return (min, max)


# Example Test Case of Ten Integers
list_int = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(list_int)

print("Pass" if ((0, 9) == get_min_max(list_int)) else "Fail")  # Pass
print("Pass" if ((0, 9) == get_min_max(list_int)) else "Fail")  # Pass
print("Pass" if ((0, 9) == get_min_max(list_int)) else "Fail")  # Pass

list_int = [i for i in range(-5, 10)]  # a list containing -5 - 9
random.shuffle(list_int)

print("Pass" if ((-5, 9) == get_min_max(list_int)) else "Fail")  # Pass

list_int = []  # an empty list
print("Pass" if ((None, None) == get_min_max(list_int)) else "Fail")  # Pass

list_int = [1]  # an list with just one element
print("Pass" if ((1, 1) == get_min_max(list_int)) else "Fail")  # Pass
