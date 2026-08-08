# Randomisation and Python Lists
import random
choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
you = input("rock, paper, scissors? ")
if computer == "rock":
    if you == "rock":
        print("Computer chose rock")
        print("Draw")
    elif you == "paper":
        print("Computer chose rock")
        print("You win")
    elif you == "scissors":
        print("Computer chose rock")
        print("You lose")
elif computer == "paper":
    if you == "rock":
        print("Computer chose paper")
        print("You lose")
    elif you == "paper":
        print("Computer chose paper")
        print("Draw")
    elif you == "scissors":
        print("Computer chose paper")
        print("You win")
elif computer == "scissors":
    if you == "rock":
        print("Computer chose scissors")
        print("You win")
    elif you == "paper":
        print("Computer chose scissors")
        print("You lose")
    elif you == "scissors":
        print("Computer chose scissors")
        print("Draw")
else:
    print("Invalid input")
