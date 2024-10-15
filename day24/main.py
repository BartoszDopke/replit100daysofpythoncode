import random

def roll_dice(number_of_sides: int):
    rolled_number = random.randint(1, number_of_sides)
    return rolled_number

while True:
    choose_number = int(input("How many sides? "))
    rolled_number = roll_dice(choose_number)
    print(f"You rolled {rolled_number}")
    choice = input("Want to try again? ")
    if choice == "yes":
        continue
    elif choice == "no":
        break
    else:
        print("You didn't say no, so let's try again!")