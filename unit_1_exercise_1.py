# Exercise 10-1
# Write a few lines summarizing what you've learned about Python in the text editor
# Write a program that reads the file and prints what you write three times
# Print the contents once by reading in the entire file,
# Once by looping over the file object
# Once by storing the lines in a list and then working with them outside the with block
print("One")
filename = 'learning_python.txt'
with open(filename) as file_object_1:
    contents = file_object_1.read()
    print(contents.rstrip())

print("\nTwo")
with open(filename) as file_object_2:
    for line in file_object_2:
        print(line.rstrip())

print("\nThree")
with open(filename) as file_object_3:
    lines = file_object_3.readlines()

for line in lines:
    print(line.rstrip())