import json

def get_stored_username():
    """Get stored username if available"""
    filename = "username.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("Enter your name: ")
    filename = "username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    if username:
        correct = input(f"Is '{username.title()}' the correct username? (y/n): ")

        if correct.lower() == 'y':
            print(f"Welcome back, {username.title()}!") 
        else:
            username = get_new_username()
            print(f"We will remember when you come back, {username.title()}")
    else:
        username = get_new_username()
        print(f"We will remember when you come back, {username.title()}")

greet_user()