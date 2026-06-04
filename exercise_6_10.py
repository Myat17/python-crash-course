# Exercise 6-10
# Make a dictionary to store each person's favorite number.
favorite_numbers = {
    'jane': 16,
    'alice': 33,
    'bob': 88,
    'john': 42,
    'charlotte': 21
}
# Print each person's name along with their favorite number.
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")