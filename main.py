# Number guessing game

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}:"))
        if guess > random_number:
            print("Sorry, your number is too high! Try again.")
        elif guess < random_number:
            print("Sorry, your number is too low! Try again.")
        elif type(guess) is str:
            raise Exception("Sorry, only numbers are allowed! Try again.")
        
    print(f"Bingo! You've got the correct number {random_number}.")

guess(10)