# Exercise 10-2
# Learning replace
# the replace() method is used to replace any word in a string with a different word
filename = 'learning_replace.txt'
with open(filename) as file_object:
    content = file_object.read()
    print("Before using replace")
    print(content)

    replace_content = content.replace('Python', 'C')
    print("\nAfter using replace")
    print(replace_content)