# For problem_world.json, problem_world2.json, and problem_world3.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not is_facing_north():
    turn_left()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    if front_is_clear():
        move()
    if not right_is_clear() and not front_is_clear():
        turn_left() 
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
