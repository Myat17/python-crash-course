# Let's create a calculator
result = float(input("Enter the first number: "))
while True:
    operator = input("Enter +, -, x, / or enter 'ac' to quit: ")

    if operator.lower() == 'ac':
        break

    number = float(input("Enter the next number: "))
 
    if operator == "+":
        result += number
    elif operator == "-":
        result -= number
    elif operator == "x":
        result *= int(number)
    elif operator == '/':
        if number == 0:
            print("Cannot divide by zero")
            continue
        result /= number
    else:
        print("Invalid operator.")
        continue

    print(f'Current result: {result}')

print(f"\nFinal result: {result}")