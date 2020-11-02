import json

try:
    fav_numb = int(input("What is your favorite number? "))
    try:
        with open("fav_nums.json", "w+") as f:
            json.dump(fav_numb, f)

    except FileNotFoundError:
        print("File not found.")

except ValueError:
    print("You provided a value that is not a number.")
    exit(1)
