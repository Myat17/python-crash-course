# Appending to a file
# Add content to a file instead of writing over existing content
# In append mode 'a', Python doesn't erase the file before returning the file object
filename = "programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.")