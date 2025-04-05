# import turtle as t

# tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

from turtle import Turtle, Screen
import random as rd

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("firebrick")

colors = ["deep sky blue", "firebrick", "medium violet red", "blue violet", "green yellow", "dark gray", "deep pink", "indian red", "light salmon", "medium spring green", "medium sea green", "dark orange", "gold", "light blue", "light coral", "light goldenrod yellow", "light green", "light pink", "light slate gray", "light steel blue", "lime green", "medium aquamarine", "medium orchid", "medium purple", "medium turquoise", "medium violet red", "midnight blue", "mint cream", "misty rose", "moccasin"]
for n in range(3, 11):
    angle = 360 / n
    turtle1.color(rd.choice(colors))
    for _ in range(n):
        turtle1.forward(100)
        turtle1.right(angle)


screen = Screen()
screen.exitonclick()

# or
# import turtle as t
# import random

# tim = t.Turtle()

# ########### Challenge 3 - Draw Shapes ########

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)