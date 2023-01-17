"""
Dice class with different sides - OOP example
Python methods/functions can have default values and can be set as shown
"""
import random

class Dice:
    def __init__(self,sides = 6): # like constructor, sides is set to 6 if size is not defined when dice instance is created
        self.sides = sides
    
    def roll(self):
        return random.randint(1, self.sides)

dice_12_side = Dice(12)
print(f'The 12 sided dice rolled: {dice_12_side.roll()}')

dice = Dice() # default size 6
for roll in range(10):
    print(dice.roll())

