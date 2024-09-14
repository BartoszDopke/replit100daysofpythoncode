superpower = input("what is your superpower? ")
cape = input("do you wear cape? ").lower()
if "fly" in superpower:
    if cape == "yes":
        print("You definitely are superman!")
    else:
        print("you are flying hero without cape!")
elif "fly" not in superpower and cape == "yes":
    print("If you don't fly, why do you need a cape?")
else:
    print("if you don't fly and don't have a cape, you are probably spiderman!")