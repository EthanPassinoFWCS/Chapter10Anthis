with open("awl.txt", "r", encoding="utf8") as awl:
    content = awl.read()

print(f"Count of 'the' {content.count('the')}")
print(f"Count of 'the ' {content.count('the ')}")
