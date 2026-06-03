# Exercise 6-6
# Polling favourite languages
favourite_languages = {
    'jane': 'python',
    'bob': 'c',
    'marina': 'matlab',
    'john': 'python'
}
friends = ['jane', 'eric', 'ruby', 'marina']
for friend in friends:
    if friend in favourite_languages:
        print(f'Thank you, {friend.title()}, for responding the poll.')
    else:
        print(f"{friend.title()}, please take the favourite languages poll.")