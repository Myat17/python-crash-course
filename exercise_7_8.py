# Exercise 7-8 (Deli)
# Make a list and fill it with the names of various sandwiches.
# Then make an empty list and loop through the list of sandwich orders
sandwich_orders = ['tuna', 'cheese', 'ham', 'hot dog']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0) # removing from the start of the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following orders are finished:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")