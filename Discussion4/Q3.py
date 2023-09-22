"""
Q3: Insect Combinatorics

An insect is inside an m by n grid. The insect starts at the bottom-left corner (1, 1) and wants to end up at the top-right corner (m, n). The insect can only move up or to the right. Write a function paths that takes the length and width of a grid and returns the number of paths the insect can take from the start to the end. (There is a closed-form solution to this problem, but try to answer it with recursion.)
"""
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m < 0 or n < 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)


