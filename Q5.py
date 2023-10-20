"""
Q5: Make Circular
Write a function make_circular that takes in a non-circular, non-empty linked list s and mutates s so that it becomes circular.
"""
def make_circular(s):
    """Mutates linked list s into a circular linked list.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> make_circular(lnk)
    >>> lnk.rest.first
    2
    >>> lnk.rest.rest.first
    3
    >>> lnk.rest.rest.rest.first
    1
    >>> lnk.rest.rest.rest.rest.first
    2
    """
    p = s
    while p.rest != Link.empty:
        p = p.rest
    p.rest = s

