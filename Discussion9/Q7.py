"""
Q7: Pow
Write the following function so it runs in ϴ(log k) time.

Hint: This can be done using a procedure called repeated squaring.
"""
def lgk_pow(n,k):
    """Computes n^k.

    >>> lgk_pow(2, 3)
    8
    >>> lgk_pow(4, 2)
    16
    >>> a = lgk_pow(2, 100000) # make sure you have log time
    """
    if k == 0:
        return 1
    res = 1
    while k:
        if k & 1:
            res *= n
        n *= n
        k >>= 1
    return res
# or    return (n if k % 2 else 1) * lgk_pow(n * n, k // 2)
