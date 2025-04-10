from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
# all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[i])
    # all_turtles.append(new_turtle)

screen.exitonclick()