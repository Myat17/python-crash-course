# Making a list of lines from a file
filename = 'pi_digits.txt'
with open(filename) as file_object:
    # readlines() method takes each line from the file and stores it in a list
    # the list is then stored in lines
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()
# can use strip() instead of rstrip() to remove the white space on the left side of the digits in each line

print(pi_string)
print(len(pi_string))