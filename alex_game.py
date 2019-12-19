# alex_GuessingGame

import random

number = random.randint(1, 10)
tries = 0
win = False 


name = input("Hello there! Welcome! Please create a username.")

print("Hello " + name + "." )

Question = input("Would you like to play a game? [y/n] ")
if Question.lower() == "n": 
    print("Thank you")
    exit()
if Question.lower() == "y":
    print("I'm thinking of a number between 1 & 10")
while not win:       
    guess = int(input("Take a guess: "))
    tries = tries + 1
    if guess == number:
        win = True    
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower")

print("Congratulations, you have guessed correctly! The number was {}".format(number))
print("It took you {} tries".format(tries))