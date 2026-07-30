# Python Functions & Karel
# Concepts Practised
# Defining and Calling Python Functions
# Indentation in Python
# While Loops


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_in_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    jump()
else:
    move()
