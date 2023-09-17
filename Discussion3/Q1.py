"""
Q1: Warm Up: Recursive Multiplication

Write a function that takes two numbers m and n and returns their product. Assume m and n are positive integers. Use recursion, not mul or *.
"""
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)

