# Handling the FileNotFoundError Exception
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exit.")

else:
    # Count the approximate number of words in the file.
    # Take the string contents, which now contains the entire text
    # Use split method to produce a list of all the words
    words = contents.split()

    # Use len() on this list to examine its length
    # Will get a good approximation of the number of words in the orginal string
    num_words = len(words)
    print(f"The file '{filename}' has about {str(num_words)} words.")