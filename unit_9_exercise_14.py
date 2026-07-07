# Exercise 9-14
# Module random contains functions that generate random numbers in a variety of ways
# The function randint() returns an integer in the range you provide
# Make a class Die with one attribute called sides that has a default value of 6
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has
# Make a 6-sided die and roll it 10 times
# Make a 10 sided die and a 20 sided die. Roll each die 10 times
from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        count = 0
        while count < 10:
            rolling = randint(1, self.sides)
            print(f"You rolled a {rolling}.")
            count += 1

die_1 = Die()
print("6-sided die:")
die_1.roll_die()
print()

die_2 = Die(10)
print("10-sided die:")
die_2.roll_die()
print()

die_3 = Die(20)
print("20-sided die:")
die_3.roll_die()