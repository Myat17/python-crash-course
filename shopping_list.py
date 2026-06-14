# Practice lists and loops
# Create a program that allows to add items to a shopping list and then print them all out nicely
shopping_list = []
while True:
    shopping_item = input("Enter your shopping item or Enter 'q' to quit: ")
    if shopping_item.lower() == 'q':
        break
    shopping_list.append(shopping_item)
    print(f"{shopping_item.title()} is added to the shopping cart.")

print("\nThe following are in the shopping cart:")
num = 1
for item in shopping_list:
        print(f"{num}. {item.title()}")
        num += 1