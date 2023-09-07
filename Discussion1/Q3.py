"""
Q3: Nearest Ten
Write a function that takes in a positive number n and rounds n to the nearest ten.

Solve this problem using an if statement.

Hint: x % 10 will get the units digit of x. For example, 1234 % 10 evaluates to 4.
"""
def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    if n % 10 >= 5:
        n += 10 - n % 10
    else:
        n -= n % 10
    return n
