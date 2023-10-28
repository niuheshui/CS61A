"""
Q12: Insert
Implement a function insert that takes a Link, a value, and an index, and inserts the value into the Link at the given index. You can assume the linked list already has at least one element. Do not return anything -- insert should mutate the linked list.
"""
def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> other_link = link
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> link is other_link # Make sure you are using mutation! Don't create a new linked list.
    True
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    Traceback (most recent call last):
        ...
    IndexError: Out of bounds!
    """
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link.rest is Link.empty:
        raise IndexError("Out of bounds!")
    else:
        insert(link.rest, value, index - 1)

# iterative solution
def insert_iter(link, value, index):
    while index > 0 and link.rest is not Link.empty:
        link = link.rest
        index -= 1
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    else:
        raise IndexError
