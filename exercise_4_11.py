# Exercise 4_11
# My Pizzas and Your Pizzas, Copying the list
my_pizzas = ['Cheese Pizza', 'Meat Pizza', 'Veggie Pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('Hawaiian')
friend_pizzas.append('Pepperoni')
print('My favorite pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza)
print("\nMy friend's favourite pizzas are:")
for fri_pizza in friend_pizzas:
    print(fri_pizza)