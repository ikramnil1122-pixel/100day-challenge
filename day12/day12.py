# Day 12 - Scope & Number Guessing Game
# Concepts Practised
# How to Modify a Global Variable
# Python Constants and Global Scope
import random


def number_guessing_game(guess, guess_number, attempts):
    if guess == guess_number:
        print(f"You got it! The answer was {guess_number}.")
        return attempts
    elif guess < guess_number:
        print("Too low.")
        return attempts - 1
    else:
        print("Too high.")
        return attempts - 1


print("I'm thinking of a number between 1 and 100")
guess = random.randint(1, 100)
choice = input("Choose hard or easy: ")
if choice == "hard":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")


while attempts > 0:
    guess_number = int(input("Make a guess: "))
    attempts = number_guessing_game(guess_number, guess, attempts)
    if guess_number == guess:
        break
    elif attempts == 0:
        print("You've run out of guesses, you lose.")
    elif guess_number != guess:
        print("Guess again.")
