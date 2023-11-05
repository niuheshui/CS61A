"""
Q3: Remove All
Write a function remove_all that takes a linked list and a value as input. This function mutates the linked list by removing all nodes that store value.

You may assume the first element of the linked list is not equal to value. You should mutate the input linked list; remove_all does not return anything.
"""
def remove_all(link, value):
    """Removes all nodes in link that contain value. The first element of
    link is never equal to value.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    pre, curr = link, link.rest
    while curr != Link.empty:
        if curr.first != value:
            pre.rest = curr
            pre = pre.rest
        curr = curr.rest
    pre.rest = curr
