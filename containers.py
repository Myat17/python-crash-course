# Tuple
# tuple = ('bob', 123, 'Lisa', ('another list'))
# list = ['bob', 123, 'Lisa', ('another list')]
# () or [] and then comma separated values
# A tuple cannot change (immutable) while you can change the values of a list

# set = {1,2,3, 'test'}
# every entry in set is unique.

# dictionary = {'name':'bob',123:"test", "Lisa": (1,2,3)}
# key:value paris instead of single entries

# a_tuple = (1, 2, 3, 'a string')
# print(a_tuple)

# a_list = [1, 2, 3, 'a string', 2]
# a_list.append('another word')
# print(a_list)
# print(list(set(a_list)))

# a_set = {1, 2, 3, 4, 4}
# print(a_set)

# a_dictionary = {'key': 'value', 123: [1, 2, 3]}
# a_dictionary['new key'] = 1.5
# print(a_dictionary)
# print(a_dictionary[123])

# # how to get values from a container
# user_list = ('Lisa', 'Bob', 'Alex', 'Anna', 'John')
# print(user_list[0:3:2])

# Exercise
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a_new_list = a_list[-9:-2:2]
# print(a_new_list)
# a_new_list.reverse()
# print(a_new_list)
a_new_list = a_list[7::-2]
print(a_new_list)