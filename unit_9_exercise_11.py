# Exercise 9-11
# Start with work from Exercise 9-8
# Store the classes User, Privileges and Admin in one module
# Create a separate file
# Make an Admin instance and call show_privileges()
from unit_9_exercise_8 import Admin

admin = Admin(
    "Bob", 
    "Carter", 
    54, 
    "Admin",
    ["can add post", "can delete post", "can ban user", "can check users' information"]
    )
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()