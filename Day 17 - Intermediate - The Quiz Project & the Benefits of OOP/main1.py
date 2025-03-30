class User: #Pascal case for class names
    
    def __init__(self):
        # Constructor method to initialize attributes
        print("New user being created...")
        self.username = None
        self.password = None

user_1 = User()
user_1.id = "001" #attribute is a variable associated with a class and object
user_1.username = "subha"
user_1.password = "password123"

print(user_1.username) # subha

user_2 = User()
user_2.id = "002"
user_2.username = "Riya"
user_2.password = "password456"

print(user_2.username) # Riya

# def function():
#     pass # This is a placeholder function