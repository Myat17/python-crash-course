# Exercise 8-3 (T-Shirt)
# Write a function that accepts a size and the text of a message that should be printed on the shirt.
def make_shirt(size, text):
    print(f"The customer wants the shirt size '{size}' with the text '{text}' printed on it.")

# Using positional argument
make_shirt("medium", "pretty girls'mantra")

# Using keyword argument
make_shirt(size= "large", text= "Number one girl")