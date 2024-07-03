class humans:
    def __init__(self):
        self.name = "shreeya"
        self.position = "Python developer"
        
    def display(self):
        print(f"my name is {self.name} and I am a {self.position}")
        
#Class humans: This is the parent class.
#_init__ Method: This special method (constructor) initializes the attributes name and position for any instance of the humans class.
#self.name = "shreeya": Sets the name attribute to "shreeya".
#self.position = "Python developer": Sets the position attribute to "Python developer".
#display Method: This method prints out the values of the name and position attributes.

        
        
class Shriya(humans):
    pass

#Class Shriya: This is the child class that inherits from the parent class humans.
#pass Statement: This indicates that the class Shriya does not add any new attributes or methods; 
# it simply inherits everything from the humans class.

s = Shriya()

#'s': This is an instance of the Shriya class. Since Shriya inherits from humans, 
#it also inherits the __init__ method, which sets s.name to "shreeya" and s.position to "Python developer".

print(s.name);print(s.position)
s.display()

#print(s.name): This prints "shreeya", the value of the name attribute inherited from the humans class.
#print(s.position): This prints "Python developer", the value of the position attribute inherited from the humans class.
#s.display(): This calls the display method, which prints "my name is shreeya and I am a Python developer".
