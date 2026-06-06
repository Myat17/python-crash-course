# Exercise 7-3
# Ask the user to enter a number and report whether the number is a multiple of 10 or not.
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")