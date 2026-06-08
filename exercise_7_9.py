# Exercise 7-9
# Use a while loop to remove all occurrences of pastrami from sandwich orders
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'cheese', 'ham', 'hot dog', 'pastrami']
finished_sandwiches = []

print("Sorry, we have run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop() # removing from the end of the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following orders are finished:")
for sandwich in finished_sandwiches:
    print(f"\t- {sandwich.title()} sandwich")