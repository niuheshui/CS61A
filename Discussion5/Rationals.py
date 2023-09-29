"""
Q1: Extending Rationals
First, fill in the following code to implement the rational ADT from lecture.
"""
from math import gcd

def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> numer(a)
    1
    >>> denom(a)
    2
    """
    d = gcd(num, den)
    return [num // d, den // d]

def numer(rat):
    """Extracts the numerator from a rational number."""
    return rat[0]

def denom(rat):
    """Extracts the denominator from a rational number."""
    return rat[1]

"""
Q2: Divide
Next, we'll be implementing two additional functions to handle operations between rational numbers.
"""
def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    return make_rat(numer(x) * denom(y), numer(y) * denom(x))

"""
Q3: Less Than
Finally, implement lt_rat(x, y), which returns True if and only if rational number x is less than rational number y.
"""
def lt_rat(x, y):
    """Returns True iff x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    return numer(x) * denom(y) < numer(y) * denom(x)
