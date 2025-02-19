def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def run_hurdle():
    while not at_goal():
        if front_is_clear():
            move()
        elif wall_in_front():
            jump()
    
run_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
