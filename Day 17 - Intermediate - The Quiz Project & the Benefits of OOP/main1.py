class User: #Pascal case for class names
    
    def __init__(self, user_id, username, password): #Constructor method
        # Constructor method to initialize attributes
        print("New user being created...")
        #attribute is a variable associated with a class and object
        self.id = user_id # self is a reference to the current instance of the class
        self.username = username
        self.password = password
        self.followers = 0 # default value for followers
        self.following = 0
    
    def follow(self, user):
        # method is a function that is associated with an object
        user.followers += 1
        self.following += 1
        
        
user_1 = User("001", "Subha", "1234") #Creating an object of the class User

# print(user_1.username) # subha
# print(user_1.followers) # 0

user_2 = User("002", "Riya", "5678") 
# can also do this:
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Riya"
# user_2.password = "5678"

# print(user_2.username) # Riya

# def function():
#     pass # This is a placeholder function

user_1.follow(user_2)
print(user_1.followers) # 0
print(user_1.following) # 1
print(user_2.followers) # 1
print(user_2.following) # 0