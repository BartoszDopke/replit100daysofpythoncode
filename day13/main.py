test_name = input("What is the name of the test? ")
max_score = int(input("What is the maximum score you could receive? "))
your_score = int(input("What is the score you have received? "))
percentage = round((your_score/max_score)*100, 2)
if int(percentage) in range(90,101):
    print("You got", percentage, "% from", test_name, "test. Wonderful!")
elif int(percentage) in range(75, 90):
    print("You got", percentage, "% from", test_name, "test. Really good!")
elif int(percentage) in range(50, 75):
    print("You got", percentage, "% from", test_name, "test. It's still not bad!")
elif int(percentage) in range(25, 50):
    print("You got", percentage, "% from", test_name, "test. You should be prepared better next time!")
else:
    print("You failed!")