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