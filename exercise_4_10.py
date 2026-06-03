# Exercise 4_10
# Slicing the pizza
fav_pizzas = ['Cheese Pizza', 'Meat Pizza', 'Veggie Pizza', 'Pepperoni', 'Hawaiian', 'Marinara','Diavola']
print('The first three items in the list are:')
print(fav_pizzas[:3])
print("\nThree items from the middle of the list are:")
middle = len(fav_pizzas) // 2
print(fav_pizzas[middle-1:middle+2])
print('\nThe last three items in the list are:')
print(fav_pizzas[-3:])