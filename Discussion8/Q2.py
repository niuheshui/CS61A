"""
Q2: Sum Nums
Write a function sum_nums that receives a linked list s and returns the sum of its elements. You may assume the elements of s are all integers. Try to implement sum_nums with recursion!
"""
def sum_nums(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if s == Link.empty:
        return 0
    return s.first + sum_nums(s.rest)
