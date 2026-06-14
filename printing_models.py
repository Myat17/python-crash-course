# Modifying a list in a function
# Start with some designs that need to be printed
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_printing = unprinted_designs.pop(0)

        # Simulte creating a 3D print from the design
        print(f"The machine is currently printing '{current_printing.title()}'.")
        completed_models.append(current_printing)

def show_completed_models(completed_models):
    """Show all the models that are printed"""

    print("\nThe following models are printed:")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs[:], completed_models) # [:] makes a copy of the list to send to the functin
show_completed_models(completed_models)