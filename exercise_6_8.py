# Exercise 6-8
# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.
pet_0 = {
    'name': 'kido',
    'kind': 'dog',
    'owner': 'jane'
}
pet_1 = {
    'name': 'poo',
    'kind': 'cat',
    'owner': 'alice'
}
pet_2 = {
    'name': 'bunny',
    'kind': 'rabbit',
    'owner': 'bob'
}
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']} owned by {pet['owner'].title()}.")
