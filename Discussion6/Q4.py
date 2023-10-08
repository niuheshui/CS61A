"""
Q4: What's the Difference?
Implement differences, a generator function that takes an iterable it whose elements are numbers. differences should produce a generator that yield the differences between successive terms of it. If it has less than 2 values, differences should yield nothing.
"""
def differences(it):
    """
    Yields the differences between successive terms of iterable it.

    >>> d = differences(iter([5, 2, -100, 103]))
    >>> [next(d) for _ in range(3)]
    [-3, -102, 203]
    >>> list(differences([1]))
    []
    """
    if len(it) < 2:
        return
    pre = next(it)
    for cur in it:
        yield cur - pre
        pre = cur

