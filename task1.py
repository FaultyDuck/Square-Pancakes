import random
idk = random.randint(1, 100)
print("Guess the number and you dont win a prize")
guess = eval(input("Give me a Number: "))
while idk != guess:
    if guess < idk:
        print("Number is Larger, guess again")
    elif guess > idk:
        print("Number is Smaller, guess again")
    guess = eval(input("Give me a Number: "))
    if guess == idk:
        print("YOU GUESSED IT WOOOOOOOOO YIPPIEEEEEEE AMAZINGGG")