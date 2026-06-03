# Exercise 6-5
# Rivers and the country each river runs through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}
for river,country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}")

print("\nThe three major rivers are:")
for river in rivers:
    print(river.title())

print("\nThree major rivers run through the following countries:")
for country in rivers.values():
    print(country.title())