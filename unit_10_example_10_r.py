# Read the stored data in JSON format
import json

filename = "numbers.json"

with open(filename, 'r') as f_obj:
    # json.load() is used to read the list back into memory
    numbers = json.load(f_obj)

print(numbers)