# Exercise 3_4 
# Create Guest list
guests = ['bob', 'john', 'austin', 'jane']
for guest in guests:
    print(f"{guest.title()}, You are invited to the dinner party.")

# Exercise 3_5
# Modify guests
print(f"{guests[1].title()} cannot come to the dinner party.")
guests[1] = "marina"
for guest in guests:
    print(f"{guest.title()}, You're invited to the dinner party.")

# Exercise 3_6
# Invite more guests
print('There will be a new place for dinner party. Invite more people.')
guests.insert(0, 'rose')
guests.insert(2, 'jasmin')
guests.append('lisa')
print(guests)
for guest in guests:
    print(f"{guest.title()}, You're invited to the bigger dinner party.")

# Exercise 3_7
# Shrinking guest list
print("The new place is no longer available and now invite only two people.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"I am sorry, {removed_guest.title()}. You are not invited to the party.")

for guest in guests:
    print(f"{guest.title()}, you are invited to the dinner party.")

guests.clear()
print(guests)