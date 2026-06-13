# Extra Exercise
# Password gate
actual_password = "Jx160196"
count = 0
while count < 5:
    enter_password = input("Enter the password:")
    if enter_password == actual_password:
        print("Welcome to our website!!!")
        break
    else:
        print("Your password is wrong. Please try again.")
    count += 1
# Explain why the program exits
if count == 5:
    print("Too many failed attempts. Access denied.")