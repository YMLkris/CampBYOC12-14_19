# Write your code here :-)
from random import randint

while True:
    # Ask user for input
    player = input('rock(r), paper(p), or scissors(s)?')

    # Have computer choose 1-3
    chosen = randint(1,3)

    # Assign letters to the random numbers

    if chosen == 1:
        computer = "r"
    elif chosen == 2:
        computer = "p"
    elif chosen == 3:
        computer = "s"

    # Write out the chosen symbols
    print("Player: " + player + " vs Computer: " + computer)

    #Determine who won

    if player == computer:
        print("It's a tie!!!")
    elif player == "r" and computer == "s":
        print("You win!!!")
    elif player == "s" and computer == "p":
        print("You Win!!!")
    elif player == "p" and computer == "r":
        print("You Win!")
    else:
        print("You Lose!!!!")








