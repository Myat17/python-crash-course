# Exercise 9-6
# Write a class called IceCreamStand that inherits from the Restaurant
# Add an attribute called flavors that stores a list of ice cream flavors
# Write a method that displays these flavors
# Create an instance of IcecreamStand and call this method
class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.name.title()} restaurant has a special {self.cuisine.title()} cuisine.")

    def open_restaurant(self):
        print(f"The {self.name.title()} restaurant is now open.")

    def read_number_served(self):
        print(f"Total {self.number_served} customers have been served today.")

# Add a method called set_number_served to set the number of customers that have been served.
    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number

# Add a method called increment_number_served to increase the number of customers who've been served.
    def increment_number_served(self, amount):
        if amount >= 0:
            self.number_served += amount

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavours = [
            "Chocolate",
            "Vanilla",
            "Strawberry",
            "ChocoMint"
        ]

    def display_flavours(self):
        print("\nAvailable Flavours:")
        for flavour in self.flavours:
            print(f"\t- {flavour}")

ice_cream = IceCreamStand("MewMew","Ice Cream")
ice_cream.describe_restaurant()
ice_cream.display_flavours()