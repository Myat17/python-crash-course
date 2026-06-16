# Exercise 8-12
# Write a function that accepts a list of items a person wants on a sandwich
# The function should have one parameter that collects as many items as the function call provides
# It should print a summary of the sandwich that is being ordered.
def make_sandwich(*ingredients):
    print("\nMaking a sandwich with:")
    
    for ingredient in ingredients:
        print(f"- {ingredient}")

    print("Your sandwich is ready!!")

make_sandwich("ham")
make_sandwich("lettuce", "grilled chicken")
make_sandwich("cheese", "tomatoes", "turkey")