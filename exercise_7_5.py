# Exercise 7-5, Movie tickets
# A movie theater charges different ticket prices depending on a person's age.
while True:
    age = input("Enter your age (or Enter 'quit' to exit the program) ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("The ticket price is $ 10.")
    else:
        print("The ticket price is $ 15.")