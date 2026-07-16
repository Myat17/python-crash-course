# Exercise 10-5
# Write a while loop that asks people why they like programming
# Each time someone enters a reason, add their reason to a file that stores all the responses
filename = 'responses.txt'

while True:
    response = input("Enter a reason why you like python or enter 'q' to quit: ")

    if response.lower() == 'q':
        break

    with open(filename, 'a') as file_object:
        file_object.write(f"I like python because {response}.\n")