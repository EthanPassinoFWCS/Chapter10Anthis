while True:
    question = input("Why do you like programming? ")
    if question == 'quit': break
    with open("programming_poll.txt", "a") as f_o:
        f_o.write(question + "\n")
