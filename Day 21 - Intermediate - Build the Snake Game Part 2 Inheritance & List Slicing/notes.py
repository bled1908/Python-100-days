# Inheritance

# class Fish(Animal):
#     def __init__(self):
#         supre().__init__() # to get hold of everything in the parent class

class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("Doing this underwater.")
    
    def swim(self):
        print("Moving in water.")
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Slicing of lists
# List slicing is a way to access a subset of elements from a list. It allows you to create a new list that contains a portion of the original list. The syntax for slicing is as follows:
# list[start:stop:step]

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[0:3])
print(piano_keys[0:7:2]) # start at 0, go to 7, take every 2nd element
print(piano_keys[::2]) # start at 0, go to end, take every 2nd element
print(piano_keys[::-1]) # start at end, go to 0, take every 2nd element (reverse the list)
print(piano_keys[::-2]) # start at end, go to 0, take every 2nd element (reverse the list and take every 2nd element)
print(piano_keys[2:]) # start at 2, go to end (take everything from 2 to end)
print(piano_keys[:3]) # start at 0, go to 3 (take everything from 0 to 3)

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[0:3])