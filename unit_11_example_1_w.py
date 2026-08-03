# Testing a function
# To learn about testing, we need code to test
# Write a simple function that takes a first and last name 
# and returns a neatly formatted full name
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name.title()
