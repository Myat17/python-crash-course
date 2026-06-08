# Exercise 7-10
# Dream vacation
dream_vacations = {}

# Set a flag to indicate that polling is active
active_polling = True

while active_polling:
    # Prompt for the user's name and destination
    user = input("Enter your name? ")
    destination = input("What is your dream destination? ")

    # Store the response in the dictionary:
    dream_vacations[user] = destination
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        active_polling = False

# Polling is complete. Show the results
print("\n--- Polling Results ---")
for user, destination in dream_vacations.items():
    if destination.lower() == 'usa' or destination.lower() == 'uk':
        print(f"{user.title()} wants to go to {destination.upper()}.")
    else:
        print(f"{user.title()} wants to go to {destination.title()}")