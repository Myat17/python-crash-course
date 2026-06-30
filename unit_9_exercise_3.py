# Exercise 9-3 (Users)
# Make a class called User
# Create two attributes called first_name and last_name
# Create several other attributes that are typically stored in a user profile
# Make a method called describe_user() that prints a summary of the user's info
# Make another method called greet_user() that prints a personalized greeting to the user
class User:
    def __init__(self,first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        # Summary of user's information
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and lives in {self.location.title()}.")
    
    def greet_user(self):
        # A personalized greeting to the user
        print(f"Hello {self.first_name.title()}! Welcome Back.")

user1 = User("tom", "johnsan", 29, "new york")
user1.describe_user()
user1.greet_user()

user2 = User('marina', 'marry', 17, "seoul")
user2.describe_user()
user2.greet_user()

user3 = User("Any", "carter", 45, "bangkok")
user3.describe_user()
user3.greet_user()