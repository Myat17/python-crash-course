# Setting a default value for an attribute
class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Create a new attribute and set value to 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self): # a new method that makes it easy to read a car's mileage
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

        
    # Modifying an attribute's value through a method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Incrementing an attribute's value through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# # Modifying an Attribute's value directly
# # Use dot notion to access the car's odometer_reading attribute and set its value directly
# my_new_car.update_odometer(100)
# my_new_car.read_odometer()

# my_new_car.update_odometer(50)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(30)
# my_new_car.read_odometer()