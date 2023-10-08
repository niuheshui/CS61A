"""
Q6: Stair Ways
In discussion 4, we considered how many different ways there are to climb a flight of stairs with n steps if you are able to take 1 or 2 steps at a time. In this problem, you will write a generator function stair_ways that yields all the different ways you can climb such a staircase.

Each "way" of climbing a staircase is represented by a list of 1s and 2s, representing the sequence of step sizes a person should take to climb the flight.

For example, for a flight with 3 steps, there are three ways to climb it:

You can take one step each time: [1, 1, 1].
You can take two steps then one step: [2, 1].
You can take one step then two steps: [1, 2]..
Therefore, stair_ways(3) should yield [1, 1, 1], [2, 1], and [1, 2] in any order.
"""
if n == 0:
        yield []
    elif n == 1:
        yield [1]
    else:
        for way in stair_ways(n - 1):
            yield [1] + way
        for way in stair_ways(n - 2):
            yield [2] + way
