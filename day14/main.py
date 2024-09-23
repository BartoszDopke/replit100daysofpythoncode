from getpass import getpass

player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")
player1_points = 0
player2_points = 0

while True:
    if player1_points == 3 or player2_points == 3:
        break
    player1_choice = getpass(f"{player1} - choose rock, paper, scissors (R,P,S): ").upper()
    player2_choice = getpass(f"{player2} - choose rock, paper, scissors (R,P,S): ").upper()
    if player1_choice == player2_choice:
        print("It's a tie!")
    elif player1_choice == "R" and player2_choice == "S" or player2_choice == "P":
        print(player1, "won this round!")
        player1_points += 1
    elif player1_choice == "P" and player2_choice == "S":
        print(player2, "won this round!")
        player2_points += 1
    elif player1_choice == "S" and player2_choice == "R":
        print(player2, "won this round!")
        player2_points += 1
    else:
        print("Someone made a wrong choice, try again!")

if player1_points > player2_points:
    print(player1, "won!")
else:
    print(player2, "won!")