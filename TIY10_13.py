import json


def get_user():
    try:
        with open("remember_me.json", "r") as h:
            g = json.load(h)
            return g
    except ValueError:
        return None


def greet_user(username=get_user()):
    print(f"Hello, {username}")


if get_user() is None:
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
