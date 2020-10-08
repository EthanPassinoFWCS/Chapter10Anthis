import json

try:
    fav_numb = int(input("What is your favorite number? "))
except ValueError:
    print("You provided a value that is not a number.")
    exit(1)

try:
    with open("fav_nums.json", "w+") as f:
        json.dump(fav_numb, f)

except FileNotFoundError:
    print("File not found.")

