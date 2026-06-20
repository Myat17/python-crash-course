students = {
    'alice': 75,
    'bob': 98,
    'john': 0,
    'jane': 95,
    'rose': 45,
    'austin': 87,
    'carter': 20
}
sorted_students = sorted(students.items(), key=lambda item: item[1])

if 0 in students.values():
    print(f"There is a 0 in the socres. Check again.")
    bottom_scores = sorted_students[1:4]
else:
    bottom_scores = sorted_students [:3]

print("Lowest 3 scores:")
for rank, (name, score) in enumerate(bottom_scores, start=1):
    print(f"\t{rank}. {name.title()}: {score}")