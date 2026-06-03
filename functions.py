# def func_name(parameters):
#   code
#   return

# Create function
# def print_x_times(parameters = 'loop', loop_amount = 5):
#     counter = 0
#     while counter <= loop_amount:
#         print(counter, parameters)
#         counter += 1
#     return "something else"

# def hypotenuse_calculator(width = 1, height = 1):
#     length = ((width)**2 + pow(height,2)) ** (1/2)
#     print(f"the length of hypotenuse is {round(length,2)}.")
#     return round(length, 2)

# # call
# # print('print')
# # test = print_x_times('smth', 4)
# # print(test)

# print(hypotenuse_calculator(width = 3, height = 4))

# Shouter function
def shouter(word = 'Hello', times = 2):
    if times <= 10:
        for i in range(times):
         print(word.upper())
    else:
       print('You are too loud')
    return 'done'
    
status = shouter()
print(status)