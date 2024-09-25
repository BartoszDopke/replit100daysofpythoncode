choice = ""
while choice != "exit":
    choice = input("What animal sound do you want to hear? ")
    if choice == "cow":
        print("Moooo!")
    elif choice == "cat":
        print("Meow!")
    elif choice == "dog":
        print("Woof woof!")
    elif choice == "exit":
        print("Bye!")
        break
    else:
        print("We do not have it in our database, try again!")