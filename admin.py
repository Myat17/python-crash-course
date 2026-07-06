from user import User

class Privileges:

    def __init__(self, privileges=None):
        # If no privileges are provided, use an empty list
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        if not self.privileges:
            print("This adminstrator has no privileges assigned.")
            return
        
        print("\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

class Admin(User):

    def __init__(self, first_name, last_name, age, position, privileges=None):
        # ***privileges is not in the parent class so that the child class cannot inherit***
        super().__init__(first_name, last_name, age, position)
        self.privileges = Privileges(privileges)