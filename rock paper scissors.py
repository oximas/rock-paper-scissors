import random


while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = ""
    while player not in choices:
        player = input("rock, paper ,or scissors: ").lower()
    print("computer:" ,computer)
    print("player:" ,player)
    if player == computer:
        print("tie")
    else:
        if(player == "rock"):
            if(computer == "paper"):
                print("YOU LOSE!")
            else: print("YOU WIN!")
        if(player == "paper"):
            if(computer == "scissors"):
                print("YOU LOSE!")
            else: print("YOU WIN!")
        if(player == "scissors"):
            if(computer == "rock"):
                print("YOU LOSE!")
            else: print("YOU WIN!")
    again = ""
    while again != "y" and again !="n":
        again = input("Do you wanna play again(Y/N)?").lower()
        if again == "n" :
            break
        elif again =="y":
            continue
    if again == "n":
        break
