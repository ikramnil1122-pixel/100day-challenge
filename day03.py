# treasure island game
print("Welcome to Treasure Island.")


print("Your mission is to find the treasure.")
choice1 = input("where do you want to go? Type 'left' or 'right' ")
if choice1 == "left":
    print("welcome to the next level")

    choice2 = input(
        "you have reached the next level. Type 'wait' to wait for a boat or 'swim' to swim across ")
    if choice2 == "wait":
        print("you have reached the next level")
        choice3 = input(
            "you have reached the next level. Type 'red', 'yellow' or 'blue' ")
        if choice3 == "red":
            print("game over")
        elif choice3 == "yellow":
            print("you win")
        elif choice3 == "blue":
            print("game over")
    else:
        print("game over")
else:
    print("Game Over")
