# Day 7 - Hangman
# concepts Practised
# How to break a Complex Problem down into a Flow Chart
# How to Check the User's Answer
# Improving the User Experience
# How to Add ASCII Art and Improve the UI

import random

# List of possible words
word_list = ["apple", "banana", "computer", "python", "orange"]

# Choose a random word
chosen_word = random.choice(word_list)

# Create blanks
display = []
for letter in chosen_word:
    display.append("_")

# Number of lives
lives = 6

print("Welcome to Hangman!")
print(" ".join(display))

# Game loop
while "_" in display and lives > 0:

    guess = input("Guess a letter: ").lower()

    # Check the guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = guess

    # If the guess is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong! You have {lives} lives left.")

    print(" ".join(display))

# Game result
if "_" not in display:
    print("🎉 You win!")

else:
    print("💀 You lose!")
    print(f"The word was: {chosen_word}")
