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
with open('text_files/welcome.txt') as file_object2:
    new_contents = file_object2.read()
    print(new_contents)