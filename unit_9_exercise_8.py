# Exercise 9-8
# Write a separate Privileges class
# The class should have one attribute, privileges() method to this class
# Make privileges instance as an attribute in the Admin class
# Create a new instance of Admin and use your method to show its privileges
class User:
    def __init__(self,first_name, last_name, age, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
    
    def describe_user(self):
        # Summary of user's information
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and works as {self.position.title()}.")
    
    def greet_user(self):
        # A personalized greeting to the user
        print(f"Hello {self.first_name.title()}! Welcome Back.")

class Privileges:

    def __init__(self, privileges=None):
        # If no privileges are provided, use an empty list
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        if not self.privileges:
            print("This adminstrator has no privileges assigned.")
            return
        
        print("\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

class Admin(User):

    def __init__(self, first_name, last_name, age, position, privileges=None):
        # ***privileges is not in the parent class so that the child class cannot inherit***
        super().__init__(first_name, last_name, age, position)
        self.privileges = Privileges(privileges)

admin = Admin(
    "Bob", 
    "Carter", 
    54, 
    "Admin",
    ["can add post", "can delete post", "can ban user", "can check users' information"]
    )
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()