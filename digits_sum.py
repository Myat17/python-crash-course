# Extra exercise
# Sum of digits
count = 0
number_sum = 0
while count < 5:
    number = input("Enter a number: ")

    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)

    number_sum += digit_sum
    count += 1
    print(f"Digit sum of {number} = {digit_sum} | Running total = {number_sum}")
    
print(f"You entered {count} numbers. Their total sum is {number_sum}.")