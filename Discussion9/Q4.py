"""
Q4: Level Mutation Link
As a reminder, the depth of a node is how far away the node is from the root. We define this as the number of edges between the root to the node. As there are no edges between the root and itself, the root has depth 0.

Given a tree t and a linked list of one-argument functions funcs, write a function that will mutate the labels of t using the function from funcs at the corresponding depth. For example, the label at the root node (with a depth of 0) will be mutated using the function at funcs.first. Assume all of the functions in funcs will be able to take in a label value and return a valid label value.

If t is a leaf and there are more than 1 functions in funcs, all of the remaining functions should be applied in order to the label of t. (See the doctests for an example.) If funcs is empty, the tree should remain unmodified.
"""
def level_mutation_link(t, funcs):
    """Mutates t using the functions in the linked list funcs.

    >>> t = Tree(1, [Tree(2, [Tree(3)])])
    >>> funcs = Link(lambda x: x + 1, Link(lambda y: y * 5, Link(lambda z: z ** 2)))
    >>> level_mutation_link(t, funcs)
    >>> t
    Tree(2, [Tree(10, [Tree(9)])])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> level_mutation_link(t2, funcs)
    >>> t2
    Tree(2, [Tree(100), Tree(15, [Tree(16)])])
    >>> t3 = Tree(1, [Tree(2)])
    >>> level_mutation_link(t3, funcs)
    >>> t3
    Tree(2, [Tree(100)])
    """
    if funcs is Link.empty:
        return
    t.label = funcs.first(t.label)
    remaining = funcs.rest
    if not t.is_leaf() and remaining is not Link.empty:
        while remaining is not Link.empty:
            t.label = remaining.first(t.label)
            remaining = remaining.rest
    for b in t.branches:
        level_mutation_link(b, remaining)

