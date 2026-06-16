# Exercise 8-14
# Write a function that stores information about a car in a dictionary
# The function should always receive a manufacturer and a model name
# It should then accept and arbitrary number of keyword arguments
def make_car(manufacturer, model, **car_info):
    car_profile = {}
    car_profile["Manufacturer"] = manufacturer.title()
    car_profile["Model name"] = model.title()

    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car = make_car('subaru', 'outback',
               color= 'blue',
               tow_package= True)
print(car)