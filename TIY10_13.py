import json
def get_user():
    try:
        with open("remember_me.json", "r") as f:
            g = json.load(f)
            return g
    except ValueError:
        return None

def greet_user(user=get_user()):
    print(f"Hello, {user}")

if get_user() == None:
    user = input("What is your user? ")
    with open("remember_me.json", "w+") as f:
        json.dump(user, f)
    greet_user(user)
else:
    c = input(f"Is {get_user()} your user (Y or N)? ").lower()
    if c == "y":
        greet_user()
    else:
        user = input("What is your user? ")
        with open("remember_me.json", "w+") as f:
            json.dump(user, f)
        greet_user(user)



