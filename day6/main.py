username = input("Provide username: ")
password = input("Provide password: ")
if username == "Bob" and password == "1234":
    print("Hi, Bob!")
elif username == "George" and password == "4321":
    print("Hello, George!")
elif username == "Jerry" and password == "5678":
    print("Good morning, Jerry!")
else:
    print("You passed wrong password or username!")