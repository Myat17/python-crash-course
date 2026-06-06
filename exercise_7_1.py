# Exercise 7-1
# Write a program that asks the user what kind of rental car they would like. 
# Print a message about that car, such as "Let me see if I can find you a Subaru."
# If the car is a BMW, print a message that says "Let me see if I can find you a BMW."
car = input("What kind of rental car would you like? ")
if car == 'bmw':
    print(f"Let me see if I can find you a {car.upper()}.")
else:
    print(f"Let me see if I can find you a {car.title()}.")