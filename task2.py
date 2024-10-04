#Create a program that takes the input from the user
#The input from the user should be saved onto a text file
#There should also be an option for the user to read or get data/info from the text file

import random

def randoRPS():
    rps = ["rock", "paper", "scissors"]
    rand = random.choice(rps)
    return rand

with open('game.txt', 'r') as file:
    content = file.read()
    print(content)

while True:
    choice = input("clear or play? ")
    if choice == 'clear':
        with open('game.txt', 'w')as file:
                file.write('')
    elif choice == 'play':
        num = input("rock paper scissors: ")
        num = num.lower()
        if num == randoRPS():
            print("Tie")
        elif num == "rock":
            if randoRPS() == "scissors":
                print("Rock beats scissors, +1 point")
                with open('game.txt', 'a')as file:
                    file.write('1')
            else:
                print("Paper beats rock, -1 point")
                with open('game.txt', 'a')as file:
                    file.write('-1')
        elif num == "paper":
            if randoRPS() == "rock":
                print("Paper beats rock, +1 point")
                with open('game.txt', 'a')as file:
                    file.write('1')
            else:
                print("Scissors beats paper, -1 point")
                with open('game.txt', 'a')as file:
                    file.write('-1')
        elif num == "scissors":
            if randoRPS() == "paper":
                print("Scissors beats paper, +1 point")
                with open('game.txt', 'a')as file:
                    file.write('1')
            else:
                print("Rock smashes scissors, -1 point") 
                with open('game.txt', 'a')as file:
                    file.write('-1')
        else:
            break
    else:
        break
