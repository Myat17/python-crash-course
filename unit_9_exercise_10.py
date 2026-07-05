# Exercise 9-10
# Using latest Restaurant class
# Store it in a module
# Make a separate file that imports Restaurant
# Make a Restaurant instance and call one of Restaurant's methods
from unit_9_exercise_6 import Restaurant, IceCreamStand

my_restaurant = Restaurant("moro", "thai")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_icecream_stand = IceCreamStand("coco", "ice cream")
my_icecream_stand.describe_restaurant()
my_icecream_stand.display_flavours()