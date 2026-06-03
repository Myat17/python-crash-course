# Exercise 6-9
# Make a dictionary to store each person's favourite places
favorite_places = {
    'jane': ['seoul', 'japan', 'thailand'],
    'alice': ['paris', 'london'],
    'marina': ['sydney', 'melbourne']
}
# Loop through the dictionary and print each person's favourite places
for name, places in favorite_places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")