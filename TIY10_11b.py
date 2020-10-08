import json

with open("fav_nums.json", "r") as f:
    print(f"I remember your favorite number is {json.load(f)}!")
