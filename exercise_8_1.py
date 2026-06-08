# Exercise 8-1
# Write a function that prints one sentence telling everyone what you are learning about.
def dispaly_message(subject):
    print(f"I am learning {subject.title()}.")

title = input("Enter what you are learning: ")
dispaly_message(title)