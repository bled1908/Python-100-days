# For problem_world.json, problem_world2.json, and problem_world3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left() 
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
