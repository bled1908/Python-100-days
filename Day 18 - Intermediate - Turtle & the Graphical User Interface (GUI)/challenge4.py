import turtle as t
import random as rd

turtle1 = t.Turtle()
t.colormode(255)  # Set the color mode to RGB
turtle1.shape("turtle")
turtle1.color("firebrick")
turtle1.pensize(8)
turtle1.speed("fastest")
turtle1.shapesize(1, 1, 3)

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(1, rd.randint(100, 200)):
    angle = rd.choice([0, 90, 180, 270])
    turtle1.color(random_color())
    turtle1.forward(20)
    # turtle1.right(angle) if rd.randint(0, 1) else turtle1.left(angle)
    turtle1.setheading(angle)


screen = t.Screen()
screen.exitonclick()
