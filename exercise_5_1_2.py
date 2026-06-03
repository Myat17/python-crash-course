# Conditional tests
car = 'toyota'
print("Is car == 'toyota'? I predict True.")
print(car == 'toyota')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

fruits = ['banana', 'apple', 'mango']
print("\nIs 'strawberry' in fruits? I predict False.")
print('strawberry' in fruits)
print("\nIs 'apple' in fruits? I predict True.")
print('apple' in fruits)

number_0 = 20
number_1 = 5
if number_0 < 25 and number_0 < 30:
    print("\nThe prediction is True.")
if number_0 > 10 or number_1 > 20:
    print("\nThe prediction is True.")
if number_0 < 10 or number_1 > 10:
    print("\nThe prediction is False.")