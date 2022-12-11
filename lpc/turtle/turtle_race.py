import turtle
import random


# The dice choose a value at random
def roll_dice():
    choice = random.randint(1, 6)
    return choice


# Move the turtles until one of them reach home
def move_turtles():

    # Sets up a for loop with a range from 1 to 20
    for i in range(20):

        #  Check if either player has reached their goal
        if player_one.pos() >= (300, 100):
            print("Player One Wins!")
            break

        elif player_two.pos() >= (300, -100):
            print("Player Two Wins!")
            break

        else:
            #  Prints out a statement asking to players
            #  to press the enter key to roll the die.
            #  The number drawn by the dice,
            #  will indicate how much the turtle will walk forward.

            # Player 1 Turn
            input("Press 'Enter' to roll the die ")
            die_outcome = roll_dice()
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20 * die_outcome)
            player_one.pendown()
            player_one.fd(20 * die_outcome)

            # Player 2 Turn
            input("Press 'Enter' to roll the die ")
            die_outcome = roll_dice()
            print("The result of the die roll is: ")
            print(die_outcome)
            print("The number of steps will be: ")
            print(20 * die_outcome)
            player_two.pendown()
            player_two.fd(20 * die_outcome)


# Painting the Player one
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)

# Painting the Player two
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# Painting the home of player one
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)

# Painting the home of player two
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

# Initiates the game
move_turtles()
