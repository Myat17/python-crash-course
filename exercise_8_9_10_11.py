# Exercise 8-9, 8-10, 8-11
# Make a list of magicians' names.
# Pass the list to a function called show_magicians() 
# which prints the name of each magician in the list
def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = f"The Great {magician_names[i].title()}"

magicians = ["migan", "aura", "john"]

great_magicians = magicians[:]

make_great(great_magicians)

print("Original magicians:")
show_magicians(magicians)

print("\nGreat magicians:")
show_magicians(great_magicians)