def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def run_hurdle():
    for _ in range(6):
        jump()
    
run_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
