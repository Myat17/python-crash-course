# Using try-except blocks
# Any code that depends on the try block executing successfully goes in the else block
print("Give two numbers to divide.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num.lower() == 'q':
        break

    second_num = input("Second number: ")
    if second_num.lower() == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print(f"The answer is {answer:.3}.")
