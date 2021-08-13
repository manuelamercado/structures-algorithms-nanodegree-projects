'''
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
'''


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    if number < 0 or number is None:
        return None
    elif number == 0:
        return 0
    elif number == 1:
        return 1

    previous = 0
    n = number // 2

    while True:
        if n * n == number:
            return n
        elif n * n < number:
            return previous - 1
        else:
            previous = n
            n = n // 2


print("Pass" if (3 == sqrt(9)) else "Fail")  # Pass
print("Pass" if (0 == sqrt(0)) else "Fail")  # Pass
print("Pass" if (4 == sqrt(16)) else "Fail")  # Pass
print("Pass" if (1 == sqrt(1)) else "Fail")  # Pass
print("Pass" if (5 == sqrt(27)) else "Fail")  # Pass
print("Pass" if (None == sqrt(-27)) else "Fail")  # Pass
print("Pass" if (None == sqrt(None)) else "Fail")  # Pass
