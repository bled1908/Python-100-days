import turtle as t
import random as rd

turtle1 = t.Turtle()
t.colormode(255)  # Set the color mode to RGB
turtle1.shape("turtle")
turtle1.color("firebrick")
turtle1.pensize(2)
turtle1.speed("fastest")
turtle1.shapesize(1, 1, 3)

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def spinograph(angle):
    for _ in range(int(360 / angle)):
        turtle1.color(random_color())
        turtle1.circle(100)
        turtle1.left(angle)
    # turtle1.left(5)

    # while turtle1.heading() != 0.0:
    #     turtle1.color(random_color())
    #     turtle1.circle(100)
    #     turtle1.left(5)

    # turtle1.circle(100)
    
    # or
    # def draw_spirograph(size_of_gap):
    # for _ in range(int(360 / size_of_gap)):
    #     tim.color(random_color())
    #     tim.circle(100)
    #     tim.setheading(tim.heading() + size_of_gap)
    
spinograph(5)

screen = t.Screen()
screen.exitonclick()
