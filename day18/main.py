from random import randint

print("Guess the number!")
guess_number = randint(0,10)
attempts = 0

while True:
    guess = int(input("Try to guess the number: "))
    if guess == guess_number:
        attempts += 1
        print(f"Congratulations! You guessed after {attempts} attempts!")
        break
    if guess < guess_number:
        attempts += 1
        print("Number is too low!")
    elif guess > guess_number:
        attempts += 1
        print("Number is too high!")
    else:
        attempts += 1
        print("You chose wrong value!")