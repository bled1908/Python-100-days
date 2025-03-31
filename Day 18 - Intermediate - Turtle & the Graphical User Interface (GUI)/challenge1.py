######## Challenge 1 - Draw a Square ############
from turtle import Turtle, Screen

turtle1 = Turtle()
turtle1.shape("turtle")
turtle1.color("firebrick")
# turtle1.right(90)
# turtle1.forward(100)
# turtle1.right(90)
# turtle1.forward(100)
# turtle1.right(90)
# turtle1.forward(100)
# turtle1.right(90)
# turtle1.forward(100)
# or
for _ in range(4):
    turtle1.right(90)
    turtle1.forward(100)

screen = Screen()
screen.exitonclick()