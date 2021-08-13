'''
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
'''


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_index = 0
    middle_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        mid_element = input_list[middle_index]

        if number == input_list[start_index]:
            return start_index
        elif number == input_list[middle_index]:
            return middle_index
        elif number == input_list[end_index]:
            return end_index
        elif number < mid_element:
            if middle_index + 1 < len(input_list):
                if mid_element < input_list[middle_index + 1]:
                    end_index = middle_index - 1
                else:
                    end_index = middle_index + 1
            elif len(input_list) == 1 and number != input_list[0]:
                return -1
        elif number > mid_element:
            if middle_index - 1 >= 0:
                if mid_element > input_list[middle_index - 1]:
                    start_index = middle_index + 1
                else:
                    start_index = middle_index - 1
            elif len(input_list) == 1 and number != input_list[0]:
                return -1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])  # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # Pass
test_function([[], -1])  # Pass
test_function([[0], 2])  # Pass
test_function([[8], 2])  # Pass
