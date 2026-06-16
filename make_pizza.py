# Passing an Arbitrary Number of Arguments
def make_pizza(size, *toppings): 
    # '*topping' tells Python to make an empty 'tuple' and pack whatever values it receives into this tuple
    # The parameter that accepts an arbitrary number of arguments must be placed last in the function definition
    """Summarize the pizza we are about to make"""
    print(f'\nMaking a {size}-inch pizza with the following toppings:')

    for topping in toppings:
        print(f'\t- {topping}')

make_pizza(25, "pepperoni")
make_pizza(32, "mushrooms", "green peppers", "extra cheese")