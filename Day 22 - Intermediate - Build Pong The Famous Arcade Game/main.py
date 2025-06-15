from turtle import Screen, Turtle
from paddle import Paddle 
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off the screen updates

r_paddle = Paddle(350, 0)  # Right paddle
l_paddle = Paddle(-350, 0)  # Left paddle
ball = Ball()
    
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Control the speed of the game
    screen.update()  # Update the screen after each segment moves
    # Here you would typically add logic for the ball movement, collision detection, etc.
    ball.move()
    
    # For now, we will just keep the game running
    pass

screen.exitonclick() 
