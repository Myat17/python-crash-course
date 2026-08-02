import json

filename = 'fav_number.json'

try:
    with open(filename) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    fav_number = input('Enter your favourite number: ')

    with open(filename, 'w') as f_obj:
        json.dump(fav_number, f_obj)

    print("I will remember your favourite number.")

else:
    print(f"I know your favourite number! It is {fav_number}.")