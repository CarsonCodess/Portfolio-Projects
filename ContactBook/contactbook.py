name = input("What is this persons name? ")
while name != "Done":
    number = input("What is their phone number? ")
    both = "Name: " + name + "    Number: " + number
    print (both)
    with open("ContactBook\contacts.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        file_object.write(both)
    name = input("What is this persons name? ('Done' to exit) ")