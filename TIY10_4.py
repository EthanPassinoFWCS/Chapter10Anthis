while True:
    with open("guest_book.txt", "a") as file_object:
        name = input("What is your name? ")
        if name == "quit": break
        file_object.write(name + "\n")
    print(f"Greetings, {name}!")
