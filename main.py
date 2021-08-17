from turtle import Turtle, Screen
from random import randint


screen = Screen()   
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'green', 'blue', 'purple', 'yellow']


turtles = {}
y = 155
for colour in colors:
    turtles[colour] = Turtle()
    turtles[colour].penup()
    turtles[colour].color(colour)
    turtles[colour].shape('turtle')
    turtles[colour].shapesize(2)
    turtles[colour].setposition(-220, y)
    y -= 60

is_game_on = True

while is_game_on:
    for colour in colors:
        if turtles[colour].xcor() > 230:
            is_game_on = False
            if colour == user_bet:
                print(f"You won! The {colour} one is winner.")
            else:
                print(f"You lost! The {colour} one is winner.")
        turtles[colour].forward(randint(0, 10))


screen.exitonclick()