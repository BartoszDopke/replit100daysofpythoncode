def ask_for_username():
    username = input("What's your username? ")
    return username

def ask_for_password():
    password = input("What's your password? ")
    return password

username = ""
password = ""

while True:
    username = ask_for_username()
    password = ask_for_password()
    if username == "admin" and password == "pass123":
        print("Login succeeded!")
        break
    else:
        print("Try again!")