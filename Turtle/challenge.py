import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.goto(-200, -200)
num_of_dot = 100
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def dots():
    for dot_count in range(1,num_of_dot+1):
        timmy.dot(20,random_color())
        timmy.forward(50)
        if dot_count%10==0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

dots()


screen = Screen()
screen.exitonclick()