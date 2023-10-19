"""
Q8: Cat Representation
Now let's implement the __str__ and __repr__ methods for the Cat class from earlier so that they exhibit the following behavior:
"""

class Pet():
    """
    >>> cat = Cat("Felix", "Kevin")
    >>> cat
    Felix, 9 lives
    >>> cat.lose_life()
    >>> cat
    Felix, 8 lives
    >>> print(cat)
    Felix
    """

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

# (The rest of the Cat class is omitted here, but assume all methods from the Cat class above are implemented)
    def __repr__(self):
        return f'{self.name}, {self.lives} lives'
    def __str__(self):
       return self.name

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives
      
       
    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(f'{self.name} says meow!')
        
        
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        if self.lives <= 0:
            self.is_alive = False
            print('This cat has no more lives to lose.')
        else:
            self.lives -= 1

        
    def revive(self):
        """Revives a cat from the dead. The cat should now have 
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print 
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            self.lives, self.is_alive = 9, True
        else:
            print('This cat still has lives to lose.')


class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()




