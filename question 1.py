name = str(input("what is your name:"))
while len(name) <= 5:
    print("user name: invalid")
    name = str(input("what is your name:"))

while name.lower() == "admin":
    print("user name: invalid")
    name = str(input("what is your name:"))

while name.strip(" ") == "":
    print("user name: invalid")
    name = str(input("what is your name:"))

print(f"welcome {name}")