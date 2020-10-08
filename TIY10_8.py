try:
    with open("cats.txt", "r") as cats:
        cat = cats.read()
    with open("dogs.txt", "r") as dogs:
        dog = dogs.read()

    print(cat)
    print(dog)
except FileNotFoundError:
    print("The file was not found.")
