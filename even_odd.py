# Extra exercise (even, odd or nothing)
number = int(input("Enter a number: "))

if number == 0:
    print(f"The number {number} is zero.")
elif number % 2 == 0:
    print(f"The number {number} is even. ({number} / 2 = {number // 2}, no reminder)")
else:
    print(f"The number {number} is odd. ({number} / 2 leaves a remainder of {number % 2})")