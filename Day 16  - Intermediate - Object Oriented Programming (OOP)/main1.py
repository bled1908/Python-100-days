# # import module1
# # print(module1.variable)

# from turtle import Turtle, Screen

# timmy = Turtle() # Create a turtle object
# print(timmy)
# timmy.shape("turtle") # Change the shape of the turtle
# timmy.color("SeaGreen1") # Change the color of the turtle
# timmy.forward(100) # Move the turtle forward by 100 units

# my_screen = Screen() # Create a screen object
# print(my_screen.canvheight) # Print the height of the screen in pixels, canvheight is a attribute of the screen object
# my_screen.exitonclick() # Close the screen when clicked

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  #calling method add_column on object table
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
# table.align["Pokemon Name"], table.align["Type"] = "l", "l"

print(table)