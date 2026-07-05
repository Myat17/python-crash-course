# Exercise 9-7
# Write a class called Admin that inherits from the User Class
# Add an attribute privileges that store a list of strings like 
# can add post, can delete post, can ban user and so on
# Write a method called show_privileges() that lists the admin's set of privileges
# Create an instance of Admin and call your method
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

class Admin(User):
    
    def __init__(self, first_name, last_name, age, position):
        super().__init__(first_name, last_name, age, position)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can check users' details"
        ]

    def show_privileges(self):
        print("\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

admin = Admin("Alice", "Marie", 34, "Admin")
admin.describe_user()
admin.greet_user()
admin.show_privileges()