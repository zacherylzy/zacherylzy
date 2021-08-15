player1 = input("Player 1 please choose Rock, Paper, or Scissors! ")
player2 = input("Player 2 please choose Rock, Paper, or Scissors! ")

if player1 == "Rock":
    print("Player 1 chose Rock!")
elif player1 == "Paper":
    print("Player 1 chose Paper!")
elif player1 == "Scissors":
    print("Player 1 chose Paper!")

elif player1 != "Rock":
    if player1 != "Scissors":
        if player1 != "Paper":
            print("Player 1 Invalid entry! Please try again")

if player2 == "Rock":
    print("Player 2 chose Rock!")
elif player2 == "Paper":
    print("Player 2 chose Paper!")
elif player2 == "Scissors":
    print("Player 2 chose Paper!")

elif player2 != "Rock":
    if player2 != "Scissors":
        if player2 != "Paper":
            print("Player 2 Invalid entry! Please try again")

if player1 == player2:
    print("It is a tie!")

elif player1 == "Paper" and player2 == "Rock":
    print("Player 1 wins (Paper beats Rock)!")

elif player1 == "Rock" and player2 == "Paper":
    print("Player 2 wins (Paper beats Rock)!")

elif player1 == "Scissors" and player2 == "Paper":
    print("Player 1 wins (Scissors beats Paper)!")

elif player1 == "Paper" and player2 == "Scissors":
    print("Player 2 wins (Scissors beats Paper)!")

elif player1 == "Rock" and player2 == "Scissors":
    print("Player 1 wins (Rock beats Scissors)!")

elif player1 == "Scissors" and player2 == "Rock":
    print("Player 2 wins (Rock beats Scissors)!")

"""
def testing_for_loops():
    a = "New Text"
    count = 0
    for i in a:
        if i == 'e':
            count = count+1
    print (count)

testing_for_loops()
"""

"""
#wrong:
player1 = input ("Let's play Rock, Paper, Scissors! Please choose one ")
player2 = input ("Now your turn to choose Rock, Paper, or Scissors! ")

if player1 == Rock:
    player1 = 1
elif player1 == Paper:
    player1 = 2
else player1 == Scissors:
    player1 = 3

if player2 == Rock:
    player2 = 1
elif player2 == Paper:
    player2 = 2
else player2 == Scissors:
    player2 = 3

if player1 > player2:
    print ("Player 1 wins!")
else:
    print ("Player 2 wins!")
"""