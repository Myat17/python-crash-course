# Exercise 9-9
# Use the final version of example 3
# Add a method to the battery class called upgrade_battery()
# This method should check the battery size and set the capacity to 85
# Make an electric car with a default battery size 
# Call get_range() once and call get_range() a second time after upgrading the battery
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

# Instances as Attributes
# Avoid adding many attributes and methods
# Create a new class called Battery that doesn't inherit from any other class
class Battery():
    """A simple attempt to model a battery for an electric car."""

# Make one parameter, battery_size in addition to self
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    # Make a method that is clearly specific to an electric car
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")

    def upgrade_battery(self):
        """Upgrade the battery to 85 kWh if it isn't already."""
        if self.battery_size < 85:
            self.battery_size = 85
            print(f"The battery has been upgraded to {self.battery_size}-kWh.")
        else:
            print("The battery is already upgraded")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge.")

# Define the child class ElectricCar
# The name of parent class must be included in parentheses in the definition of the child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    # Take in the information required to make a car instance
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        # super() function is a special function that helps Python make connection
        # between the parent and child class
        super().__init__(make, model, year)
        # Initialize attributes specific to an electric car
        self.battery = Battery()

    # Override methods from the Parent Class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()