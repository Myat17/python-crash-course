# Exercise 10-3
# Write a program that prompts the user for their name
# When they respond, write their name to a file called guest.txt

filename = 'guest.txt'

# Create the file (or overwrite it)
with open(filename,'w') as file_object:
    name = input("Enter your name: ")
    file_object.write(name + "\n")

# Append another guest
while True:
    name = input("Enter your name or enter 'q' to quit the program: ")

    if name.lower() == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")

    print(f"{name} has been added.")

with open(filename, 'r') as file_object:
    print(repr(file_object.readlines()))