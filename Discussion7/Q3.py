"""
Q3: Keyboard
Below is the definition of a Button class, which represents a button on a keyboard. It has three attributes: pos (numerical position of the button on the keyboard), key (the letter of the button), and times_pressed (the number of times the button is pressed).

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0
We'd like to create a Keyboard class that takes in an arbitrary number of Buttons and stores these Buttons in a dictionary. The keys in the dictionary will be ints that represent the position on the Keyboard, and the values will be the respective Button. Fill out the methods in the Keyboard class according to each description.
"""
class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard stores an arbitrary number of Buttons in a dictionary. 
    Each dictionary key is a Button's position, and each dictionary
    value is the corresponding Button.
    >>> b1, b2 = Button(5, "H"), Button(7, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[5].key
    'H'
    >>> k.press(7)
    'I'
    >>> k.press(0) # No button at this position
    ''
    >>> k.typing([5, 7])
    'HI'
    >>> k.typing([7, 5])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for b in args:
            self.buttons[b.pos] = b

    def press(self, pos):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        res = ''
        if pos in self.buttons:
            b = self.buttons[pos]
            b.times_pressed += 1
            res = b.key
            
        return res

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        res = ''
        for pos in typing_input:
            res += self.press(pos)
        return res
      


