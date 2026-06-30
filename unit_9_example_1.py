# Creating and using a Class
# You can model almost anything using classes
# Creating the Dog class
class Dog(): # Define a class called Dog
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        # __init__ is a special method Python runs automatically whenever we create
        # a new instance based on the Dog class.
        # current __init__ has three parameters: self, name and age
        # self parameter is required in the method definition, and must come first before the other parameters
        
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        # Any variable prefixed with self is available to every method in the class
        # self.name takes the value stored in the parameter name and stores it in the variable name
        # which is attached to the instance being created. Same for self.age
        # Variables that are accessible through instances like this are called attributes

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")
    # The Dog class has two other methods defined: sit() and roll_over().
    # These methods don't need additional information like a name or age
    # we just define them to have one parameter, self.

my_dog = Dog('willie', 6)
# We tell Python to create a dog whose name is willie and whose age is 6
# When Python reads this line, it calls __init__method in Dog with the arguments willie and 6.
# The __init__ method creates an instance representing this particular dog and sets the
# name and age attributes using the values we provided.
print(f"My dog's name is {my_dog.name.title()}.")
# Access the value of my_dog's attribute name by writing my_dog.name
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()