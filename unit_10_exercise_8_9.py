# Exercise 10-8 and 10-9
# Make two files, cats.txt and dogs.txt
# Store at least three names of cats and three names of dogs
# Write a program to read these files and print the contents of the file to the screen
# Wrap your code in a try-except block to catch the FileNotFoundError
# Print a friendly message if a file is missing
# Move one of the files to a different location on your system
# Make sure the code in the except block excutes properly
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading {filename}")

    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        #pass
        print(f"Sorry, the file {filename} is not found.")
    else:
        print(contents)