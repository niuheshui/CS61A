"""
Q7: Unique Digits
Write a function that returns the number of unique digits in a positive integer.

Hints: You can use // and % to separate a positive integer into its one's digit and the rest of its digits.

You may find it helpful to first define a function has_digit(n, k), which determines whether a number n has digit k.
"""
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    unique = 0
    i = 0
    while i < 10:
        if has_digit(n, i):
            unique += 1
        i += 1
    return unique

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n > 0:
        last = n % 10
        n = n // 10
        if last == k:
            return True
    return False


