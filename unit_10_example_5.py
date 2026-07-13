# Writing to an empty file
# Writing over existing content
# Python erase the file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    # open() has two arguments, one is filename 
    # the second 'w' tells Python that we want to open the file in write mode
    # 'r' is read mode (default), 'a' is append mode
    # 'r+' allows to read and write to the file
    file_object.write("I love learning Python.\n")
    file_object.write("I love learning new things.\n")

    # open() function automatically creates the file you're writing to if it doesn't already exit
    # Be careful opening a file in write mode ('w')
    # if the file does exit, Python will erase the file before returning the file object

    # Python can only write strings to a text file.
    # If you want to store numerical data in a text file, convert the data to string format first