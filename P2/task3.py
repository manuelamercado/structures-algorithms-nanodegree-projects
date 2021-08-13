'''
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(n log(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
'''


def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    items = mergesort(input_list)
    num1 = []
    num2 = []
    
    for index, num in enumerate(items):
        if index == 0 or index % 2 == 0:
            num1.append(num)
        else:
            num2.append(num)
    
    result = []
    num1 = int(''.join([str(num) for num in num1]))
    num2 = int(''.join([str(num) for num in num2]))
    result.append(num1)
    result.append(num2)

    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])  # Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  # Pass
test_function([[1,0,0,0,0,0,0,0,0], [10000, 0000]])  # Pass
test_function([[0,0,0,0,0,0,0,0,0], [00000, 0000]])  # Pass
