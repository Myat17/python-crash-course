# Importing specific functions
from pizza import make_pizza
make_pizza(16, "pepperoni")
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a function an Alias
from pizza import make_pizza as mp
mp(10, "pepperoni")
mp(18, 'mushrooms', 'green peppers', 'extra cheese')

# Importing an entire module
import pizza
pizza.make_pizza(25, 'mushrooms')
pizza.make_pizza(32, 'pepperoni', 'extra cheese')

# Using as to give a module an alias
import pizza as p
p.make_pizza(8, "pepperoni")
p.make_pizza(12, "extra cheese", 'mushrooms')

# Importing all functions in a module
from pizza import *
make_pizza(8, "pepperoni")
make_pizza(12, "extra cheese", 'mushrooms')