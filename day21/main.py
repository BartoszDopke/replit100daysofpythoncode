print("""
It is the multiplication table. 
I'm going to increase the number you will choose from 1 to 10. 
Let's see if you can stil do maths!""")

points = 0
number = int(input("Name your multiplies: "))

for i in range(1,11):
    j = i * number
    answer = int(input(f"{i} x {number} = "))
    if answer == j:
        print("Correct!")
        points += 1
    else:
        print(f"No, the answer is {j}")
        break

if points == 10:
    print(f"Congratulations! You scored {points} out of 10!")
else:   
    print(f"You scored {points} out of 10.")