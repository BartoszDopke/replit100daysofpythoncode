print("Let's see if you can guess the lyrics!")
lyrics = ""
attempts = 0
while True:
    print("All I am is a ___, I want the world in my hands!")
    lyrics = input("What are the lyrics? ")
    if lyrics == "man":
        attempts += 1
        print("Wow, you made it on", attempts, "attempt!")
        break
    else:
        attempts += 1
        print("Try again!")