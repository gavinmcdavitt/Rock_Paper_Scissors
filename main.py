import random
import sys
import cv2
from PIL import Image

print("You are about to play rock paper scissors. I hope you do not lose!\n"
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors Scissors wins\n"
      + "Paper vs Scissors Scissors wins")

def playGame(number, score):
    if number <= 3:
        choice = int(input("Pick a number between 1 and 3\n" +
                           "1. Rock, 2. Paper, 3. Scissors\n"))
        comp = random.randint(1, 3)
        print("The computer has selected: ")
        if comp == 1:
            print("Rock ")
        if comp == 2:
            print("Paper")
        if comp == 3:
            print("Scissors")
        if (choice == 1 and comp == 1) or (choice == 2 and comp == 2) or (choice == 3 and comp == 3):
            print("Tie game")
        elif (choice == 1 and comp == 2) or (choice == 2 and comp == 3) or (choice == 3 and comp == 1):
            print("Computer wins!")
            score -= 1
        elif (choice == 1 and comp == 3) or (choice == 2 and comp == 1) or (choice == 3 and comp == 2):
            print("User wins!")
            score += 1
        print("Score:", score)
        return score
    else:
        choice = int(input("Pick a number between 1 and 3\n" +
                           "1. Rock, 2. Paper, 3. Scissors\n"))

        if choice == 1:
            print("The computer has selected: ")
            print("Paper!")

        if choice == 2:
            print("The computer has selected: ")
            print("Scissors!")

        if choice == 3:
            print("The computer has selected: ")
            print("Rock!")

        print("User loses")
        score -= 1
        print("Score is ", score)
        return score

score =0
while True:
    #gives a 70% chance of a game that the user will automatically lose.
    number = random.randint(1, 10)
    score = playGame(number, score)


