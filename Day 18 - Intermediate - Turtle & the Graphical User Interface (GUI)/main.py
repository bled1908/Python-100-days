# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)

import colorgram as cg
import os
import turtle as t
import random as rd

turtle1 = t.Turtle()
t.colormode(255)  # Set the color mode to RGB

turtle1.pensize(2)
turtle1.speed("fastest")
turtle1.hideturtle()

image_path = os.path.join(os.path.dirname(__file__), 'image.jpg')
colors_objects = cg.extract(image_path, 35)

colors = []

for color in colors_objects:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors.append((r, g, b))
    

i = 0
forw_dis = 0
turtle1.setheading(270)
turtle1.penup()
turtle1.forward(200)
turtle1.setheading(180)
turtle1.forward(200)
turtle1.setheading(0)
pos = turtle1.position()

for _ in range(10):
    for _ in range(10):
        turtle1.dot(20, colors[i])
        turtle1.penup()
        turtle1.forward(50)
        i += 1
        i = i % len(colors)
        
    x = pos[0]
    y = pos[1]
    turtle1.setx(x)
    turtle1.sety(y)
    turtle1.setheading(90)
    forw_dis += 50
    turtle1.forward(forw_dis)
    turtle1.setheading(0)
    

screen = t.Screen()
screen.exitonclick()

# or
# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)









# screen = turtle_module.Screen()
# screen.exitonclick()