# Exercise 6-7
# Create different people from differnt cities
people_0 = {
    'first_name': 'marina',
    'last_name': 'carter',
    'age': 20,
    'city': 'new york'
}
people_1 = {
    'first_name': 'ruby',
    'last_name': 'jane',
    'age': 30,
    'city': 'seoul'
}
people_2 = {
    'first_name': 'rose',
    'last_name': 'park',
    'age': 18,
    'city': 'new zealand'
}

people = [people_0, people_1, people_2]

for person in people:
    username = f"{person['first_name']} {person['last_name']}"
    print(f"{username.title()} ({person['age']}), lives in {person['city'].title()}")