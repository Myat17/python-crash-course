# Exercise 8-2
# Favourite book
# Write a function that accepts one parameter, title
def favourite_book(title):
    print(f"One of my favorite books is {title.title()}.")

book = input("Enter your favourite book: ")
favourite_book(book)