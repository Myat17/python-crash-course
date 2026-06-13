# Exercise 8_6 (City Names)
# Write a function called city_country and it should return a string formatted like "Santiago, Chile"
def city_country(city, country):
    formatted_name = f"{city}, {country}"
    return formatted_name.title()

print(city_country("bangkok", "thailand"))
print(city_country("seoul", "korea"))
print(city_country("tokyo", "japan"))