# Exercise 8-5 (Cities)
# Make a function that accepts the name of a city and its country
def describe_city(city, country= "thailand"):
    print(f"{city.title()} is in {country.title()}")

describe_city("bangkok")
describe_city("phuket")
describe_city(city= "tokyo", country= "japan")