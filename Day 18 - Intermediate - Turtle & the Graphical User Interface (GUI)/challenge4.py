
from turtle import Turtle, Screen
import random as rd

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("firebrick")

colors = ["deep sky blue", "firebrick", "medium violet red", "blue violet", "green yellow", "dark gray", "deep pink", "indian red", "light salmon", "medium spring green", "medium sea green", "dark orange", "gold", "light blue", "light coral", "light goldenrod yellow", "light green", "light pink", "light slate gray", "light steel blue", "lime green", "medium aquamarine", "medium orchid", "medium purple", "medium turquoise", "medium violet red", "midnight blue", "mint cream", "misty rose", "moccasin"]

turtle1.pensize(8)
turtle1.speed(8)
turtle1.shapesize(1, 1, 3)
for _ in range(1, rd.randint(100, 200)):
    angle = rd.choice([0, 90, 180, 270])
    turtle1.color(rd.choice(colors))
    turtle1.forward(20)
    # turtle1.right(angle) if rd.randint(0, 1) else turtle1.left(angle)
    turtle1.setheading(angle)


screen = Screen()
screen.exitonclick()
