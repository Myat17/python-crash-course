# Refactoring
# Improve the code by breaking it up into a series of functions that have specific jobs
# Refactoring makes the code cleaner, easier to understand and easier to extend

import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'users.json'

    try:
        with open(filename) as f_obj:
            usernames = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return usernames

def get_new_username():
    """Prompt for new usernames"""
    usernames = []
    
    while True:
        username = input("Enter your name or 'q' to quit: ")
    
        if username.lower() == 'q':
            break
    
        usernames.append(username)
    
        if usernames:
            with open("users.json", 'w') as f_obj:
                json.dump(usernames, f_obj, indent=2)
            print("Usernames have been saved.")

        return usernames

def greet_user():
    """Greet the user by name"""
    usernames = get_stored_username()

    if usernames:
        for username in usernames:
            print(f"Welcome back, {username.capitalize()}!")
    else:
        usernames = get_new_username()

        for username in usernames:
            print(f"We will remember you when you come back, {username.capitalize()}!")
    

greet_user()