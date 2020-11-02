try:
    a = int(input("Give me the first number to add: "))
    b = int(input("Give me the second number to add: "))
    print(a + b)
except ValueError:
    print("The value that you entered is not a number.")
    exit(0)
