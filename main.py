# imports ===========================
from color_list import colors_list
import turtle as t
import random as ran

turt = t.Turtle()
t.colormode(255)
turt.speed("fastest")

# change position in canvas for the lower left corner
# pen not needed since using the dot function
turt.penup()
turt.hideturtle()
turt.goto(-250, -250)

# ==================================

for i in range(10):

    for j in range(10):
        turt.dot(20, ran.choice(colors_list))
        turt.forward(50)

    if i % 2 == 0:
        turt.dot(20, ran.choice(colors_list))
        turt.left(90)
        turt.forward(50)
        turt.left(90)

    else:
        turt.dot(20, ran.choice(colors_list))
        turt.right(90)
        turt.forward(50)
        turt.right(90)

screen = t.Screen()

screen.exitonclick()
