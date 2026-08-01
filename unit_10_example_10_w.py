# Storing data
# json module allows to dump simple Python data structures into a file
# and load the data from that file next time the program runs
# json can also be used to share data between different Python programs
# JSON data format is not specific to Python, can share data with people who work in other programming languages

import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_object:
    # json.dump() is used to store the set of number or a list of numbers
    json.dump(numbers, f_object)