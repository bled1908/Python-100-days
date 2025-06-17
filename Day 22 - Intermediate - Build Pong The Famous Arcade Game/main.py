from turtle import Screen
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

# Store key states
keys_pressed = {
    "Up": False,
    "Down": False,
    "w": False,
    "s": False
}

# Key press/release handlers
def key_press_up(): keys_pressed["Up"] = True
def key_release_up(): keys_pressed["Up"] = False
def key_press_down(): keys_pressed["Down"] = True
def key_release_down(): keys_pressed["Down"] = False
def key_press_w(): keys_pressed["w"] = True
def key_release_w(): keys_pressed["w"] = False
def key_press_s(): keys_pressed["s"] = True
def key_release_s(): keys_pressed["s"] = False

game_score = screen.textinput("Game Score", "Enter the score to win the game (default is 5):")

# Bind keys 
screen.listen()
screen.onkeypress(key_press_up, "Up")
screen.onkeyrelease(key_release_up, "Up")
screen.onkeypress(key_press_down, "Down")
screen.onkeyrelease(key_release_down, "Down")
screen.onkeypress(key_press_w, "w")
screen.onkeyrelease(key_release_w, "w")
screen.onkeypress(key_press_s, "s")
screen.onkeyrelease(key_release_s, "s")
    

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the game
    screen.update()  # Update the screen after each segment moves
    # Here you would typically add logic for the ball movement, collision detection, etc.
    
    # Handle paddle movement based on key states
    if keys_pressed["Up"]:
        r_paddle.move_up() 
    if keys_pressed["Down"]:
        r_paddle.move_down()
    if keys_pressed["w"]:
        l_paddle.move_up()
    if keys_pressed["s"]:
        l_paddle.move_down()
    
    # Ball movement
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
        
    # Check for game over condition
    if scoreboard.score_l >= int(game_score) or scoreboard.score_r >= int(game_score):
        game_is_on = False
        if scoreboard.score_l > scoreboard.score_r:
            scoreboard.goto(0, 0)
            scoreboard.write("Left Player Wins!", align="center", font=("Courier", 24, "normal"))
        elif scoreboard.score_r > scoreboard.score_l:
            scoreboard.goto(0, 0)
            scoreboard.write("Right Player Wins!", align="center", font=("Courier", 24, "normal"))
        else:
            scoreboard.goto(0, 0)
            scoreboard.write("It's a Tie!", align="center", font=("Courier", 24, "normal"))

screen.exitonclick() 
