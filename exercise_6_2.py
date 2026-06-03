# Exercise 6-2
# People's favourite numbers
favourite_numbers = {
    'ruby': 16,
    'bob': 9,
    'myat': 8,
    'marina': 67,
    'john' : 1
}
for name, number in favourite_numbers.items():
    print(f"{name.title()}'s favourite number is {number}.")