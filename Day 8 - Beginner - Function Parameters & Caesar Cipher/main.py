# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# # Simple function
# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Goodbye")
    
# greet()

# Function that allows for input

def greet_with_name(name): # name is the parameter
    print(f"Hello {name}")
    print(f"How are you {name}?")
    
greet_with_name("Subhadeep") # Subhadeep is the argument

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")