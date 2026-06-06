# Exercise 7-4
# Write a loop that prompts the user to enter a series of pizza toppings unit they enter a 'quit' value. 
prompt = '\nEnter a pizza topping that you would like to add to your pizza: '
prompt += "\nEnter 'quit' when you are finished. "
topping = ''
while topping.lower() != 'quit':
    topping = input(prompt)
    print(topping)