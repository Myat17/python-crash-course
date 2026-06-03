# Exercise 4_3
# print to count 1 to 20 inclusive
for num in range(1,21):
    print(num)

# Exercise 4_4 & 4_5
# Count one million and sum
million = list(range(1, 1000001))
print(sum(million))
print(max(million))
print(min(million))

# Exercise 4_6
# Odd numbers using third argument of range()
for odd_num in range(1,21,2):
    print(odd_num)

# Exercise 4_7
# Multiples of 3 from 30
for number in range(1,11):
    mul_three = number * 3
    print(mul_three)
