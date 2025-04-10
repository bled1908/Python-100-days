from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Movement speed
MOVE_DISTANCE = 10

# Key press tracking
keys_pressed = {
    "w": False,
    "s": False,
    "a": False,
    "d": False,
    "p": False
}

def move():
    if keys_pressed["w"]:
        tim.forward(MOVE_DISTANCE)
    if keys_pressed["s"]:
        tim.backward(MOVE_DISTANCE)
    if keys_pressed["a"]:
        tim.setheading(tim.heading() + 10)
    if keys_pressed["d"]:
        tim.setheading(tim.heading() - 10)
    if keys_pressed["p"]:
        tim.penup()
    else:
        tim.pendown()
    screen.ontimer(move, 100)  # Repeat every 100 ms

def key_press_w(): keys_pressed["w"] = True
def key_release_w(): keys_pressed["w"] = False

def key_press_s(): keys_pressed["s"] = True
def key_release_s(): keys_pressed["s"] = False

def key_press_a(): keys_pressed["a"] = True
def key_release_a(): keys_pressed["a"] = False

def key_press_d(): keys_pressed["d"] = True
def key_release_d(): keys_pressed["d"] = False

def key_press_p(): keys_pressed["p"] = True
def key_release_p(): keys_pressed["p"] = False

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Key press bindings
screen.onkeypress(key_press_w, "w")
screen.onkeyrelease(key_release_w, "w")
screen.onkeypress(key_press_s, "s")
screen.onkeyrelease(key_release_s, "s")
screen.onkeypress(key_press_a, "a")
screen.onkeyrelease(key_release_a, "a")
screen.onkeypress(key_press_d, "d")
screen.onkeyrelease(key_release_d, "d")
screen.onkeypress(key_press_p, "p")
screen.onkeyrelease(key_release_p, "p")

# Also bind uppercase if needed
screen.onkey(clear, "c")
screen.onkey(clear, "C")

screen.listen()
move()  # Start polling
screen.mainloop()