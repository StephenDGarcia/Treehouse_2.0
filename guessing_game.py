"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""
import random


def start_game():
    answer = random.randint(1, 10)
    count = 1
    print("Welcome player, let's play a guessing game")
    guess = input("Pick a number between 1 and 10:  ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a number")
    else:
        while guess != answer:
            count += 1
            if guess > answer:
                print("It's lower, try again")
                guess = int(input("Enter a new number: "))
            else:
                print("It's higher, try again")
                guess = int(input("Enter a new number: "))
        print("Got it! It took you {} tries \n GAME OVER".format(count))


start_game()
"""
again = input("Would you like to play again Y/N? ")
if again == "Y":
    start_game()
else: 
    sys.exit(0)
"""