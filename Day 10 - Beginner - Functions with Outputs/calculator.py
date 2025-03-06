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
first_result = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_result}")

operation_symbol = input("Pick another operation: ")
num3 = float(input("What's the next number?: "))
second_result = operations[operation_symbol](first_result, num3)

print(f"{first_result} {operation_symbol} {num3} = {second_result}") 