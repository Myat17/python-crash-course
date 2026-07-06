# Exercise 9-12
# Store the User class in one module
# Store Privileges and Admin classes in a separate module
# In a separate file, create an Admin instance and call show_privileges() to show everything is working correctly
from admin import Admin
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