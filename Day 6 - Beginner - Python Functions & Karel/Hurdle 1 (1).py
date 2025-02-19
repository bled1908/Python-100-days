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
    number_of_hurdles = 6
    while number_of_hurdles > 0:
        jump()
        number_of_hurdles -= 1
        print(number_of_hurdles)
    
run_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
