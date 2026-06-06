# Exercise 7-6, Three Exits
# Different version of either Exercise 7-4 or Exercise 7-5
prompt = '\nEnter a pizza topping that you would like to add to your pizza: '
prompt += "\nEnter 'quit' when you are finished. "

# Use a conditional test in the while statement to stop the loop
# topping = ''
# while topping.lower() != 'quit':
#     topping = input(prompt)

#     if topping.lower() != 'quit':
#         print(f"{topping.title()} has been added to your pizza.")


# Use an active variable to control how long the loop runs
# active = True
# while active:
#     topping = input(prompt)

#     if topping.lower() == 'quit':
#         active = False
#     else:
#         print(f'{topping.title()} has been added to your pizza.')


# Use a break statement to exit the loop when the user enters a 'quit' value
while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        break
    else:
        print(f"{topping.title()} has been addded to your pizza.")