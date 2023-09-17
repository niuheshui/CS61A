"""
Q4: Is Prime

Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise. Assume n > 1. We implemented this in Discussion 1 iteratively, now time to do it recursively!
"""
def f(n, m):
    if m > n // m:
        return True
    else:
        return n % m != 0 and f(n, m + 1)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    #return f(n, 2)
    def check_all(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        return check_all(i + 1)
    return check_all(2)
