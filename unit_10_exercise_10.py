def word_count(filename, word):

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"The file {filename} is not found.")
    else:
        count = contents.lower().count(word.lower())
        print(f"The word '{word}' appears {count} times in the text file.")

filename = 'OpenFOAM.txt'
word_count(filename, "CFD")
word_count(filename, "OpenFOAM")