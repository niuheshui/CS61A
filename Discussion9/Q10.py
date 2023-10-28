"""
Q10: Mint
A mint is a place where coins are made. In this question, you'll implement a Mint class that can output a Coin with the correct year and worth.

Each Mint instance has a year stamp. The update method sets the year stamp of the instance to the present_year class attribute of the Mint class.
The create method takes a subclass of Coin (not an instance!), then creates and returns an instance of that class stamped with the mint's year (which may be different from Mint.present_year if it has not been updated.)
A Coin's worth method returns the cents value of the coin plus one extra cent for each year of age beyond 50. A coin's age can be determined by subtracting the coin's year from the present_year class attribute of the Mint class.
"""
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2023
    >>> dime = mint.create(Dime)
    >>> dime.year
    2023
    >>> Mint.present_year = 2103  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2023
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2102
    >>> Mint.present_year = 2178     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2023

    def __init__(self):
        self.update()

    def create(self, coin):
        return coin(self.year)

    def update(self):
        self.year = self.present_year



class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        y = Mint.present_year - self.year - 50
        return self.cents + (y if y > 0 else 0)

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

