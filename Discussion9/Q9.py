"""
Q9: Partitions
Tree-recursive generator functions have a similar structure to regular tree-recursive functions. They are useful for iterating over all possibilities. Instead of building a list of results and returning it, just yield each result.

You'll need to identify a recursive decomposition: how to express the answer in terms of recursive calls that are simpler. Ask yourself what will be yielded by a recursive call, then how to use those results.

Definition. For positive integers n and m, a partition of n using parts up to size m is an addition expression of positive integers up to m in non-decreasing order that sums to n.

Implement partition_gen, a generator functon that takes positive n and m. It yields the partitions of n using parts up to size m as strings.

Reminder: For the partitions function we studied in lecture (video), the recursive decomposition was to enumerate all ways of partitioning n using at least one m and then to enumerate all ways with no m (only m-1 and lower).
"""
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield n
    if n - m > 0:

        for par in partition_gen(n - m, m):
            yield f'{par} + {m}'

    if m > 1:
        yield from partition_gen(n, m - 1)


