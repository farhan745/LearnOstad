#Write option
with open("new.text", "w") as  file:
    file.write("Hello Guys!"*3)
    print("Created")
#Read Option
with open("../list_tuple.text", "r") as file:
    content = file.read()
    print(content)