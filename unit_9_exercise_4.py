# Exercise 9-4
# Start program from Exercise 9-1
# Add attribute called number_served with a default value of 0
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


restaurant1 = Restaurant('mandarin palace', 'chinese')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant1.read_number_served()

restaurant1.set_number_served(5)
restaurant1.read_number_served()

restaurant1.increment_number_served(15)
restaurant1.read_number_served()