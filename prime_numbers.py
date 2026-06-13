# Extra exercises
# Write a function to check the number is prime or not
def prime(num):
    if num < 2:
        print(f"{num} is not a prime number.")
        return 
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return # Exit if the answer is already know. There is no need to keep checking
    print(f"{num} is a prime number.")

number = int(input("Enter a number: "))
check_number = prime(number)