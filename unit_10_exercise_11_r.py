import json

filename = 'fav_numbers.json'

with open(filename) as f_obj:
    fav_number = json.load(f_obj)

print(f"I know your favourite number is {fav_number}!")