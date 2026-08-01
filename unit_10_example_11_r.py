import json
filename = 'users.json'

with open(filename) as f_obj:
    usernames = json.load(f_obj)

print("The following users have been saved: ")

for username in usernames:
    print(f"\t-{username.capitalize()}")