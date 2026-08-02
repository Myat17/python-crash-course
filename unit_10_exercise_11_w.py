import json

filename = 'fav_numbers.json'

fav_number = int(input("Enter your favourite number: "))

with open(filename, 'w') as f_obj:
    json.dump(fav_number, f_obj)

print("I will remember your favourite number.")