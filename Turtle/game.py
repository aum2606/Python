import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(800, 800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-250, -150, -50, 50, 150, 250]
turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-300, y=y_positions[turtle_index])
    turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 370:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have won, the {winner} is the winner")
            else:
                print(f"You have lost, the {winner} is the winner")

        random_dist = random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()
