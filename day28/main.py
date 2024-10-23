import os, random, time

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


name1 = set_name()
type1 = set_type()
health_stats_name1 = health_stats_generator()
strength_stats_name1 = strength_stats_generator()
os.system("cls")
print(f"Your character name is {name1} which is type of {type1}. It has {health_stats_name1} health points and {strength_stats_name1} strength points.")
print("Now it's time for an opponent!")
name2 = set_name()
type2 = set_type()
health_stats_name2 = health_stats_generator()
strength_stats_name2 = strength_stats_generator()
os.system("cls")
print(f"Your character name is {name2} which is type of {type2}. It has {health_stats_name2} health points and {strength_stats_name2} strength points.")
if strength_stats_name1 > strength_stats_name2:
    hit_points = strength_stats_name1 - strength_stats_name2 + 1
else:
    hit_points = strength_stats_name2 - strength_stats_name1 + 1
time.sleep(3)
print("It's time for the battle!")

while True:
    os.system("cls")
    print(f"""---HEALTH STATS---
    Name: {name1}
    HP: {health_stats_name1}

    Name: {name2}
    HP: {health_stats_name2}
------------------
    """)

    health_stats_name1 -= hit_points
    print(f"{name1} got hit!")
    time.sleep(2)
    health_stats_name2 -= hit_points
    print(f"{name2} was not able to miss a hit!")
    if health_stats_name1 <= 0:
        print(f"{name2} has won!")
        break
    elif health_stats_name2 <= 0:
        print(f"{name1} has won!")
        break
