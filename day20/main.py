starting_point = int(input("What's your starting point? "))
ending_point = int(input("What's your ending point? "))
increment = int(input("By which number it should increment? "))

for i in range(starting_point, ending_point, increment):
    print(f"Current number is {i}")