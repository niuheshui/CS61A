"""
Q7: Make Your Own Lambdas
For the following problem, first read the doctests for functions f1, f2, f3, and f4. Then, implement the functions to conform to the doctests without causing any errors. Be sure to use lambdas in your function definition instead of nested def statements. Each function should have a one line solution.
"""
def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: 3

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: lambda x: lambda: x


