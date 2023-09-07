"""
Q5: Make Keeper
Implement make_keeper, which takes a positive integer n and returns a function f that takes as its argument another one-argument function cond. When f is called on cond, it prints out the integers from 1 to n (including n) for which cond returns a true value when called on each of those integers. Each integer is printed on a separate line.
"""
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    return f
