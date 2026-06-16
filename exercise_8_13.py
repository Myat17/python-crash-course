# Using Arbitrary Keyword Arguments
# An Arbitrary number of arguments will be accepted but you don't know a head of time what kind of information will be passed
def build_profile(first, last, **user_info):
    # **user_info cause Python to create an empty 'dictionary' and pack whatever name-value paries it receives into this dictionary
    profile = {}
    profile["first_name"] = first.title()
    profile["last_name"] = last.title()

    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile("Myat", "Thin",
                             location= "thailand",
                             position= "product specialist",
                             field= "wind tunnels")
print(user_profile)