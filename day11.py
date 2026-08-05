# The Blackjack Capstone Project
# Concepts Practised
# Refactoring and calling procedures


import random
cart = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def draw():
    e = random.choice(cart)
    your_cards.append(e)


def draw_computer():
    while sum(computer_cards) < 17:
        f = random.choice(cart)
        computer_cards.append(f)


def result():
    if sum(your_cards) > 21 and 11 in your_cards:
        your_cards.remove(11)
        your_cards.append(1)
    resulte_you = sum(your_cards)
    if sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
    resulte_computer = sum(computer_cards)
    return resulte_you, resulte_computer


def compare(resulte_you, resulte_computer):
    if resulte_you > 21:
        print("you went over. you lose")
    elif resulte_computer > 21:
        print("computer went over. you win")
    elif resulte_you == 21 and resulte_computer == 21:
        print("draw")
    elif resulte_you > resulte_computer:
        print("you win")
    else:
        print("you lose")


[a, b] = random.choice(cart, 2)
[c, d] = random.choice(cart, 2)
your_cards = [a, b]
computer_cards = [c, d]

print(f'your cards is:[{a} : {b}]')
print(f'the computer\'s first cards is:[{c} : {'*'}]')
game_over = False
while not game_over:
    if result_computer() == 21:
        print("computer has a blackjack. you lose")

    input = str(input(
        'type n if you want to draw another card or type s if you want to stop drawing cards'))
    if input == 'n':
        draw()
    else:
        compare()
