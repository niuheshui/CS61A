"""
Q2: Paths List
(Adapted from Fall 2013) Fill in the blanks in the implementation of paths, which takes as input two positive integers x and y. It returns a list of paths, where each path is a list containing steps to reach y from x by repeated incrementing or doubling. For instance, we can reach 9 from 3 by incrementing to 4, doubling to 8, then incrementing again to 9, so one path is [3, 4, 8, 9].
"""
def paths(x, y):
    """Return a list of ways to reach y from x by repeated
    incrementing or doubling.
    >>> paths(3, 5)
    [[3, 4, 5]]
    >>> sorted(paths(3, 6))
    [[3, 4, 5, 6], [3, 6]]
    >>> sorted(paths(3, 9))
    [[3, 4, 5, 6, 7, 8, 9], [3, 4, 8, 9], [3, 6, 7, 8, 9]]
    >>> paths(3, 3) # No calls is a valid path
    [[3]]
    >>> paths(5, 3) # There is no valid path from x to y
    []
    """
    if x > y:
        return []
    elif x == y:
        return [[y]]
    else:
        a = paths(x+1, y)
        b = paths(x*2, y)
        return [[x] + subpath for subpath in a + b]

