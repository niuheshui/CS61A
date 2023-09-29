# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree's list of branches is empty, and False otherwise."""
    return not branches(tree)

def print_tree(t, depth = 0):
    print('  ' * depth + str(label(t)))
    for branch in branches(t):
        print_tree(branch, depth + 1)

"""
Q5: Height
Write a function that returns the height of a tree. Recall that the height of a tree is the number of non-root nodes in the longest path from the root to a leaf.
"""
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    if is_leaf(t):
        return 0
    return max([height(b) for b in branches(t)]) + 1

"""
Q6: Find Path
Write a function find_path that takes in a tree t with unique labels and a value x. It returns a list containing the labels of the nodes along the path from the root of t to the node labeled x.
"""
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [x]
    else:
        path = [p for p in [find_path(b, x) for b in branches(t)] if p]
        if path:
            return [label(t)] + path[0]

"""
Q7: Sprout Leaves
Define a function sprout_leaves that takes in a tree, t, and a list of leaf labels, leaves. It produces a new tree that is identical to t, but where each old leaf node has new branches, for each label in leaves.
"""
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t), [tree(leaves) for leaves in leaves])
    else:
        return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])

"""
Q8: Perfectly Balanced
Part A: Implement sum_tree, which returns the sum of all the labels in tree t.
"""
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    return label(t) + sum([sum_tree(b) for b in branches(t)])

"""
Part B: Implement balanced, which returns whether every branch of t has the same total sum and that the branches themselves are also balanced.
"""
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    return is_leaf(t) or all([(sum_tree(b) == sum_tree(branches(t)[0])) and balanced(b) for b in branches(t)]) 
