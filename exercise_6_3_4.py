# Exercise 6-4
# Create a glossary dictionary with 10 Python terms.
glossary = {
    "variable": "A name that stores a value.",
    "string": "A sequence of characters enclosed in quotes.",
    "list": "A collection of items stored in a particular order.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "Repeats a block of code multiple times.",
    "tuple": "An immutable collection of ordered items.",
    "boolean": "A data type with only two values: True or False.",
    "class": "A blueprint for creating objects.",
    "object": "An instance created from a class."
}

for term, meaning in glossary.items():
    print(f"{term.title()}:")
    print(f"\t{meaning}\n")