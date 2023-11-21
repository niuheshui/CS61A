# Q1: Virahanka-Fibonacci
Write a function that returns the n-th Virahanka-Fibonacci number.

# Q2: List Making
Let's make some Scheme lists. We'll define the same list with list, quote, and cons.

The following list was visualized using the draw feature of code.cs61a.org.

# Q3: List Concatenation
Write a function which takes two lists and concatenates them.

Notice that simply calling (cons a b) would not work because it will create a deep list. Do not call the builtin procedure append, since it does the same thing as list-concat should do.

# Q4: Map
Write a function that takes a procedure and applies it to every element in a given list using your own implementation without using the built-in map function.

# Q5: Remove
Implement a procedure remove that takes in a list and returns a new list with all instances of item removed from lst. You may assume the list will only consist of numbers and will not have nested lists.

Hint: You might find the built-in filter procedure useful (though it is definitely possible to complete this question without it).

You can find information about how to use filter in the 61A Scheme builtin specification!

# Q6: List Duplicator
Write a Scheme function, duplicate that, when given a list, such as (1 2 3 4), duplicates every element in the list (i.e. (1 1 2 2 3 3 4 4)).
