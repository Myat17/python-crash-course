# ChainMap class manages a sequence of dictionaries 
# it combines multiple dictionaries into one logical view
# it searches through them in the order they are given to find values associated with keys
import collections
a = {'a': 'A', 'c': 'C', 'd': 'D'}
b = {'b': 'B', 'c': 'D', 'd': 'E'}

m = collections.ChainMap(a, b)
print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print('d = {}'.format(m['d']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))