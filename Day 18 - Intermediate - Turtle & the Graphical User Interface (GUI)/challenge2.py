########### Challenge 2 - Draw a Dashed Line ########
from turtle import Turtle, Screen

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("firebrick")

for _ in range(10):
    turtle1.forward(10)
    turtle1.penup()
    turtle1.forward(10)
    turtle1.pendown()
    # you can also change color to seem like it's not drawing but it's not efficient

screen = Screen()
screen.exitonclick()