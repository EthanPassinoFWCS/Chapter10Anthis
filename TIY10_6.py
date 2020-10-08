try:
    a = int(input("Give me the first number to add: "))
    b = int(input("Give me the second number to add: "))
except ValueError:
    print("The value that you entered is not a number.")
    exit(0)

print(a + b)
