# Exercise 5-8
# Admin report
usernames = ['Eric', 'Jane', 'Admin', 'Bobby', 'Yang', 'Lisa']
for username in usernames:
    if username.lower() == 'admin':
        print(f"Hello, {username.title()}, would you like to see a status report?")
    else:
        print(f"Hello, {username.title()}, thank you for logging in again.")