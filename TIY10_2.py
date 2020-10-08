file = "learning_python.txt"

with open(file, "r") as file_object:
    contents = file_object.read()

print(contents)
new_contents = contents.replace("python", "C#")
print(new_contents)
