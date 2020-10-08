f = open("learning_python.txt", "w+")
f.write("In python you can create dictionaries.")
f.write("\n")
f.write("In python you can create lists.")

f.close()

f = open("learning_python.txt", "r")
lines = f.readlines()

for line in lines:
    print(line)


with open("learning_python.txt", "r") as file_object:
    contents = file_object.read()
print(contents)

with open("learning_python.txt", "r") as file_object:
    for line in file_object:
        print(line)
