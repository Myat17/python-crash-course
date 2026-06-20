students = {
    'alice': 67,
    'bob': 98,
    'john': 0,
    'jane': 95,
    'rose': 45,
    'austin': 87,
    'carter': 32
}
sorted_students = sorted(students.items(), key=lambda item: item[1], reverse=True)
# key=lambda item: item[1] tells Python to sort by the score (the second item in each pair)
# Not by the name
top_three = sorted_students[:3]

average_score = 0

print("Top Three students: ")
for rank, (name, score) in enumerate(top_three, start=1):
    print(f"\t{rank}. {name.title()} {score}")
    average_score += score

average_score /= len(top_three)
print(f"\nAverage score of top 3: {average_score:.2f}")