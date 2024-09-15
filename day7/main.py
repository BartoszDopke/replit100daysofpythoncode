start = input("Are you true fan of Harry Potter? ").lower()
if start == "yes":
    print("That's great, let's find out!")
    ron = input("Tell me full name of Harry's best friend: ")
    if ron == "Ron Weasley":
        print("Nice! Another question!")
    elif ron == "Ron":
        print("You forgot about surname, but it's okay")
    else:
        print("No, it was wrong")
    hermione = input("Who's his second best friend? ")
    if hermione == "Hermione Granger":
        print("Great! One more question!")
    elif hermione == "Hermione":
        print("You forgot about surname, but it's okay")
    else:
        print("No, it was wrong")
    voldemort = input("Who's his biggest enemy? ")
    if voldemort.capitalize() == "Voldemort":
        print("Great, you're real fan!")
    else:
        print("Oops, you were wrong, but at least you knew that", ron, "and", hermione, "were his best friends!")
else:
    print("Alright, thanks for being honest with me!")