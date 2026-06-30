# Exercise 9-5
# Add an attribute called login_attempts to User class from Exercise 9-3
class User:
    def __init__(self,first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def display_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("tom", "johnsan", 29, "new york")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.display_login_attempts()

user1.reset_login_attempts()
user1.display_login_attempts()