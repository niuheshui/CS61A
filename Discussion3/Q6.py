"""
Q6: Merge Numbers 

Write a procedure merge(n1, n2), which takes numbers with digits in decreasing order and returns a single number with all of the digits of the two in decreasing order. Any number merged with 0 will be that number (treat 0 as having no digits). Use recursion.
"""
def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0 or n2 == 0:
        return n1 if n2 == 0 else n2
    
    if n1 % 10 > n2 % 10:
        n1, n2 = n2, n1
    return merge(n1 // 10, n2) * 10 + n1 % 10
   
