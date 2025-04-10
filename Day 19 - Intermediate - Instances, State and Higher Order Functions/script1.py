from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

# Event listener
screen.listen() #listen to the keyboard input
screen.onkey(key = "space", fun = move_forwards) #when we use a function as a argument, we don't use the parentheses as we don't want to call the function, we want to pass it as a reference
# It has keyword arguments
screen.exitonclick() 

# Example of using a function as an argument
def add(a, b):
    return a + b

def calculate(a, b, func): #func is a function that takes two arguments and returns a value
    # It has positional arguments
    return func(a, b)
# Here calculate is a higher order function because it takes a function as an argument

result = calculate(2, 3, add) #we pass the add function as an argument to the calculate function
print(result) #5