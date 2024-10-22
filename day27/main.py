import os, random

def set_name():
    name = input("Name your character: ")
    return name

def set_type():
    type = input("Choose character type: ")
    return type

def health_stats_generator():
    six_dice_roll = random.randint(1,6)
    twelve_dice_roll = random.randint(1,12)
    return (six_dice_roll + twelve_dice_roll) / 2 + 10

def strength_stats_generator():
    six_dice_roll = random.randint(1,6)
    twelve_dice_roll = random.randint(1,12)
    return (six_dice_roll + twelve_dice_roll) / 2 + 12


while True:
    name = set_name()
    type = set_type()
    health_stats = health_stats_generator()
    strength_stats = strength_stats_generator()
    os.system("cls")
    print(f"Your character name is {name} which is type of {type}. It has {health_stats} health points and {strength_stats} strength points.")
    choice = input("Do you want to generate another character? ")
    if choice.lower() == "yes":
        os.system("cls")
        continue
    else:
        break