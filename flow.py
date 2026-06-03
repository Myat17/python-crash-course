# if statements
# if 3 > 4:
#     print('correct result')
# elif 0 > 1:
#     print('some other result 1')
# elif 0 == 0 and 5 > 1:
#     print('some other result 2')
#     if len([1, 2, 3]) > 2:
#         print('list is long enough')
# else:
#     print('incorrect result')

# while loop
# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         print('counter is 5')
# print('while loop has finished')

# for loop 
# only working for every single entry of some kind of container
# test_list = {1, 2, 3, 4, 5, 3}
# for x in test_list:
#     print(x)

# Truthy and falsy
# if '':
#     print('truthy')
# else:
#     print('falsy')

# Exercise
exercise_list = [1, 2, 3, 4, 5]
exercise_counter = 0
for x in exercise_list:
    print(x)
    if x == 2:
        print('the value is 2')
    else:
        print('the value is not 2')
while exercise_counter <= 6:
    print('last item')
    exercise_counter +=1