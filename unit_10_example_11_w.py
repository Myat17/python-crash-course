# Saving and reading user-generated data
import json

filename = 'users.json'

# Need to bring the exisiting memory first
# append mode is not valid in JSON file
# JSON file must contain one valid JSON value
# If you append multiple JSON values, the file becomes invalid

# The stardard workflow with JSON is
# Read the existing data
# Modify it in memory
# Write the complete updated data back to the file.

# load existing usernames if the file exists
try:
    with open(filename) as f_obj:
        usernames = json.load(f_obj)
except FileNotFoundError:
    usernames = []

while True:
    username = input("Enter your name or 'q' to quit: ")

    if username.lower() == 'q':
        break

    usernames.append(username)

# Save the updated list
with open(filename, 'w') as f_obj:
    json.dump(usernames, f_obj, indent=2)

print("Usernames have been saved")