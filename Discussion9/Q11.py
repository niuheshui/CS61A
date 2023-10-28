"""
Q11: Every Other
Implement every_other, which takes a linked list s. It mutates s such that all of the odd-indexed elements (using 0-based indexing) are removed from the list. For example:
"""
def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    if s is Link.empty or s.rest is Link.empty :
        return
    s.rest = s.rest.rest
    every_other(s.rest)
    


