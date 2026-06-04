# Exercise 6-11
# Make a dictonary called cities and store information about three cities.
cities = {
    'new york': {
        'country': 'usa',
        'population': 8478072,
        'fact': 'a city and state full of history and suprising quirks'
    },
    'guangzhou': {
        'country': 'china',
        'population': 73600000,
        'fact': 'a historic and vibrant city blending ancient traditions with modern innovation'
    },
    'tokyo': {
        'country': 'japan',
        'population': 37040000,
        'fact': 'a vibrant metropolis where ancient traditions meet futuristic innovation'
    }
}
# Print the name of each city and all of the information stored about it.
for city in cities:
    print(f"\n{city.title()}:")
    city_info = cities[city]
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].capitalize()
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")