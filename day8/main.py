name = input("What's your name? ")
day = input("What day is today? ").capitalize()

if day == "Monday":
    print("Monday is the beginning of the week!")
elif day == "Tuesday":
    print("First day has passed, now it's Tuesday!")
elif day == "Wednesday":
    print("It's the middle of the week,", name, "!")
    choice = input("Are you happy? yes/no ").lower()
    while choice not in ["yes", "no"]:
        print("Wrong choice, try again!")
        choice = input("Are you happy? yes/no ").lower()
    if choice == "yes":
        print("Me too!")
    else:
        print("Don't worry, weekend is coming!")
elif day == "Thursday":
    print("It's past the middle of the week already!")
elif day == "Friday":
    print("TGIF!")
elif day == "Saturday":
    print("How do you feel after Friday party?")
elif day == "Sunday":
    print("Get some rest, Monday is coming",name,"!")
else:
    print("it doesn't sound like the day of the week!")

