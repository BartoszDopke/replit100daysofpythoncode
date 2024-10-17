import random

def roll_dice(number: int):
    rolled_number = random.randint(1, number)
    return rolled_number

def roll_two_dices():
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,8)
    return first_dice * second_dice

print("Character Stats Generator")
while True:
    hp = roll_two_dices()
    name = input("Name your character: ")
    print(f"Character Name: {name}")
    print(f"HP: {hp}")
    choice = input("Do you want to add new character? ")
    if choice.lower() == "yes":
        continue
    else:
        break