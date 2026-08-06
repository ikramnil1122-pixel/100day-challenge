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


def blackjack(cards):
    return len(cards) == 2 and sum(cards) == 21


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
    if blackjack(your_cards) and blackjack(computer_cards):
        print("both have blackjack. draw")
    elif blackjack(your_cards):
        print("blackjack! you win")
    elif blackjack(computer_cards):
        print("computer blackjack! you lose")
    elif resulte_you > 21:
        print("you went over. you lose")
    elif resulte_computer > 21:
        print("computer went over. you win")
    elif resulte_you == resulte_computer:
        print("draw")

    elif resulte_you > resulte_computer:
        print("you win")
    elif resulte_you < resulte_computer:
        print("you lose")
    else:
        print("draw!")


[a, b] = random.choices(cart, k=2)
[c, d] = random.choices(cart, k=2)
your_cards = [a, b]
computer_cards = [c, d]
print(f'your cards is:{your_cards}')
print(f'the computer\'s cards is:[{computer_cards[0]}, ?]')
if blackjack(your_cards) or blackjack(computer_cards):
    print("your_cards is:", your_cards)
    print("the computer's cards is:", computer_cards)
    resulte_you, resulte_computer = result()
    compare(resulte_you, resulte_computer)
    game_over = True
else:
    game_over = False

while not game_over:
    choice = input(
        'type n if you want to draw another card or type s if you want to stop drawing cards')
    if choice == 'n':
        draw()
        print(f'your cards is:{your_cards}')
        resulte_you, resulte_computer = result()
        if resulte_you > 21:
            print(f"computer's cards is:{computer_cards}")
            compare(resulte_you, resulte_computer)
            game_over = True
        else:
            continue
    else:
        draw_computer()
        resulte_you, resulte_computer = result()
        print(f'your cards is:{your_cards}')
        print(f'the computer\'s cards is:{computer_cards}')
        compare(resulte_you, resulte_computer)
        game_over = True
