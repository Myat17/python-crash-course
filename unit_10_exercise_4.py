# Exercise 10-4
# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen
# And add a line recording their visit in a file called guest_book.txt
# Make sure each entry appears on a new line in the file
filename = 'guest_book.txt'

while True:
    name = input("Enter your name or enter 'q' to quit the program: ")

    if name.lower() == 'q':
        break

    print(f"Hello, {name}! Nice to meet you!")

    with open(filename, 'a') as file_object:
        file_object.write(f"{name} visited the guest book.\n")

with open(filename, 'r') as file_object:
    print(repr(file_object.readlines()))