"""
Q8: Match Maker
Implement match_k, which takes in an integer k and returns a function that takes in a variable x and returns True if all the digits in x that are k apart are the same.

For example, match_k(2) returns a one argument function that takes in x and checks if digits that are 2 away in x are the same.

match_k(2)(1010) has the value of x = 1010 and digits 1, 0, 1, 0 going from left to right. 1 == 1 and 0 == 0, so the match_k(2)(1010) results in True.

match_k(2)(2010) has the value of x = 2010 and digits 2, 0, 1, 0 going from left to right. 2 != 1 and 0 == 0, so the match_k(2)(2010) results in False.

Important: You may not use strings or indexing for this problem. You do not have to use all the lines; one staff solution does not use the line directly above the while loop.

Hint: Floor dividing by powers of 10 gets rid of the rightmost digits.
"""
def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def match(n):
        BASE = 10 ** k
        while n >= BASE:
            if n % BASE != (n // BASE) % BASE:
                return False
            n //= BASE
        return True
    return match


