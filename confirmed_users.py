# Moving items from one list to another
# Start with users that need to be verified
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verified each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users
while unconfirmed_users: # loop will run as long as the list unfonfirmed_users is not empty
    current_user = unconfirmed_users.pop() # Remove unverified users one at a time from the end

    print(f"Verfying user; {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())