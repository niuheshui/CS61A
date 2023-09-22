"""
Q1: Count Stair Ways

Imagine that you want to go up a flight of stairs that has n steps, where n is a positive integer. You can take either one or two steps each time you move. In how many ways can you go up the entire flight of stairs?
"""
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    if n == 0 or n == 1:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)

