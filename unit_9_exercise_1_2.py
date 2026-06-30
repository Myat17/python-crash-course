# Exercise 9-1 (Restaurants)
# Make a class called Restaurant
# __init__ method should store two attributes: name and cuisine type
# Make a method called describe_restaurant() that prints these pieces of information
# Make a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class.
# Print the two attributes individually, and then call both methods

class Restaurant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"The {self.name.title()} restaurant has a special {self.cuisine.title()} cuisine.")

    def open_restaurant(self):
        print(f"The {self.name.title()} restaurant is now open.")

restaurant1 = Restaurant('mandarin palace', 'chinese')
print(f'The restaurant near my home is {restaurant1.name.title()}')
print(f"Its {restaurant1.cuisine} cuisine is very popular.")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()


# Exercise 9-2
restaurant2 = Restaurant('gianni ristorante', 'italian')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Que Pasa', "Mexican")
restaurant3.describe_restaurant()