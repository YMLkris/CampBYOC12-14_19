# Write your code here :-)
from random import randint
myScore = 0
compScore = 0

while myScore < 5 and compScore < 5 :
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
        myScore +=1
    elif player == "s" and computer == "p":
        print("You Win!!!")
        myScore +=1
    elif player == "p" and computer == "r":
        print("You Win!")
        myScore +=1
    else:
        print("You Lose!!!!")
        compScore +=1
    print("The Current Score Is You:" + str(myScore) + " Computer:"+ str(compScore))



