import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("circle")
# timmy.color("red")
# turtle.pensize(5)


#
# def draw_shape(num_side):
#     angle = 360/num_side
#     for _ in range(num_side):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
#

# direction = [0,45,90,135,180,225,270,315]
# for _ in range(20):
#     timmy.forward(50)
#     timmy.setheading(random.choice(direction))


#

turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#
# for _ in range(20):
#     timmy.color(random_color())
#     timmy.forward(random.randint(30, 100))
#     timmy.right(random.randint(0, 360))
timmy.speed("fastest")


def draw_spiro(size_gap):
     for _ in range(int(360/size_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)


draw_spiro(5)
screen = Screen()
screen.exitonclick()
