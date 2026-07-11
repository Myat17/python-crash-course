# Reading from a file
# Reading an Entire file
# First, need open() function to open the file to access
# The open() function needs one argument: the name of the file to open
# open('pi_digits.txt') returns an object representing the file
# Python stores this object in file_object

with open('pi_digits.txt') as file_object:

    # Use read() method to read the entire content of the file 
    # And store it as one long string in contents
    contents = file_object.read()

    # rstrip() removes the extra blank line at the end of the output
    print(contents.rstrip())

# open file from different file path
# this only works when text_files is located inside the same folder with the .py file
with open('text_files/welcome.txt') as file_object2:
    new_content_1 = file_object2.read()
    print(new_content_1)

# Try to open file from any location on the computer
# Try to use "/" in Windows in file paths if using "\" shows an error
file_path = 'C:/Users/MSI/Downloads/python.txt'
with open(file_path) as file_object3:
    new_content_2 = file_object3.read()
    print(new_content_2)