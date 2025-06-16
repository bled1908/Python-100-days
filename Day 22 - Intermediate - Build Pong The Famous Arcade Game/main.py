from turtle import Screen, Turtle
from paddle import Paddle 
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off the screen updates

r_paddle = Paddle(350, 0)  # Right paddle
l_paddle = Paddle(-350, 0)  # Left paddle
ball = Ball()
scoreboard = Scoreboard()
    
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the game
    screen.update()  # Update the screen after each segment moves
    # Here you would typically add logic for the ball movement, collision detection, etc.
    ball.move() 
    # Detect collision with upper and lower walls and bounce the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect R paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.increase_left_score()
        
    # Detect L paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.increase_right_score()

screen.exitonclick() 
