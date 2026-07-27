# Extercise 10-6 and 10-7
# Addition
while True:
    first_num = input("Enter first number or 'q' to quit: ")
    if first_num.lower() == 'q':
        break

    second_num = input("Enter second number or 'q' to quit: ")
    if second_num.lower() == 'q':
        break

    try:
        total = int(first_num) + int(second_num)
    except ValueError:
        print("Please enter a number.")
    else:
        print(f"The sum of {first_num} and {second_num} is {total}.")