# Exercise 9-13
# Start with Exercise 6-4
# Rewrite program using the OrderedDict class in the standard library
# Make sure the order of the output matches the order in which key-values pairs were added to the dictionary

# Import the OrderedDict class from the module collections
from collections import OrderedDict

# Create an instance of the OrderedDict class and store this instance in glossary
glossary = OrderedDict()

# No curly brackets
# the call to OrderedDict() creates an empty ordered dictionary and stores it in glossary
# Then, add each term and meaning to glossary one at a time
glossary["variable"] = "A name that stores a value."
glossary["string"] = "A sequence of characters enclosed in quotes."
glossary["list"] = "A collection of items stored in a particular order."
glossary["dictionary"] = "A collection of key-value pairs."
glossary["function"] = "A reusable block of code that performs a specific task."
glossary["loop"] = "Repeats a block of code multiple times."
glossary["tuple"] = "An immutable collection of ordered items."
glossary["boolean"] = "A data type with only two values: True or False."
glossary["class"] = "A blueprint for creating objects."
glossary["object"] = "An instance created from a class."

for term, meaning in glossary.items():
    print(f"{term.title()}:")
    print(f"\t{meaning}\n")