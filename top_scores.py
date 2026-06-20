scores = [66, 45, 89, 32, 99, 78, 86, 95]

# Sorted the scores from highest to lowers
sorted_scores = sorted(scores, reverse=True)

# Choose top three scores from sorted scores
top_scores = sorted_scores[:3]

print("Top 3 scores:")
for rank, score in enumerate(top_scores, start=1):
    # enumerate() gives both positon and the value while looping start=1
    # makes the count begin at 1 instead of Python's default 0
    print(f"{rank}. {score}")