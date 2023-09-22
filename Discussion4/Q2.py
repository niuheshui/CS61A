"""
Q2: Count K

Consider a special version of the count_stair_ways problem where we can take up to k steps at a time. Write a function count_k that calculates the number of ways to go up an n-step staircase. Assume n and k are positive integers.
"""
def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
   
    if n < 0:
        return 0
    if n < 2:
        return 1
    i, res = 1, 0
    while i <= k:
        i, res = i + 1, res + count_k(n - i, k)
    return res

