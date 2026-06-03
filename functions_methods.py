# # Functions
# print('a value')
# input('ask for a value')
# function_name('argument') >>> value

# # methods -> functions of datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('e','3'))

# # new functions
# print(abs(-1))
# print(max(10, 5))
# print(min(10, 5))
# print(len('test'))

# Pythagoream theorem
width = int(input('Enter the width of the triangle: '))
height = int(input('Enter the height of the triangle: '))
length = ((width)**2 + pow(height,2)) ** (1/2)
print(f"the length of hypotenuse is {round(length,2)}.")