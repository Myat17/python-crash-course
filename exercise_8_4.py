# Exercise 8-4 (Large Shirts)
# Write a function that accepts a size and the text of a message that should be printed on the shirt.
# Modify the funciton so that shirts are large by default with a message that reads I love Python
def make_shirts(size= "large", text= "I love Python"):
    print(f"The customer wants the shirt size '{size}' with the text '{text}' printed on it.")

make_shirts()
make_shirts(size='medium')
make_shirts(size= 'large', text= 'Number one girl')