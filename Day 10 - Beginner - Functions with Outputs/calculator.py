# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide 
def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero")
        return
    return n1 / n2

# Power
def power(n1, n2):
    return n1 ** n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}

num1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("What's the second number?: "))


print(f"{num1} {operation_symbol} {num2} = {operations[operation_symbol](num1, num2)}")