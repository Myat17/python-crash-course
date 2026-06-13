# Making an argument optional
def get_formatteed_name(first_name, last_name, middel_name= ''): # middle name is optional, so it's listed last in the definition and its default value is an empty string.
    """Return a full name, neatly formatted."""
    if middel_name: # if middle name evaluates to true if a middle name argument is in the function call
        full_name = f"{first_name} {middel_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatteed_name('jennie', 'kim', 'rubyjane')
print(musician)

musician = get_formatteed_name("jimi", "carter")
print(musician)

# Returning a dictionary
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Jennie', 'Kim', age='30')
print(musician)

# using a function with a while loop
def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("(Enter 'quit' at any time to quit)")
    f_name = input("First name: ")
    if f_name.lower() == 'quit':
        break
    l_name = input("Last name: ")
    if l_name.lower() == 'quit':
        break
    name = formatted_name(f_name, l_name)
    print(f"Hello, {name}")