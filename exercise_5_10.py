# Exercise 5-10
# Checking usernames
current_users = ['Bob', 'marina', 'Jane', 'alex', 'mira', 'John']
new_users = ['lisa', 'jane', 'JOHN', 'rose', 'jasmin']

# Change all the usernames in current_users to lowercase
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The name {user.title()} is already in use. Enter a new name.")
    else:
        print(f"The username {user.title()} is available.")