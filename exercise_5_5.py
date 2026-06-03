alien_color = input("Enter the color of alien to shoot down: ")
if alien_color.lower() == 'green':
    print("The player just earned 5 points.")
elif alien_color.lower() == 'yellow':
    print("The player just earned 10 points.")
else:
    print("The player just earned 15 points.")