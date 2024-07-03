class house:
    colour = None
    size = None
    
    def __init__(self,color,size):
        self.color = color
        self.size = size
        
    def display(self):
        pass
    
#Class house: This is the parent class.
#Class Attributes: colour and size are class attributes, initially set to None. They are shared across all instances of the class.
#__init__ Method: This special method (constructor) initializes the instance attributes color and size with values provided when an instance is created.
#self.color = color: Sets the instance attribute color.
#self.size = size: Sets the instance attribute size.
#display Method: This method is defined but not implemented (pass is a placeholder indicating that this method does nothing in the parent class).
    
    
class Shreeyahouse(house):
    def __init__(self,color,size):
        self.color = color + " color"
        self.size = size + " BHK"
        
    def display(self):
        print(f"Shreeya's house is  {self.color} and she lives in {self.size}")
        
#Class Shreeyahouse: This is the child class that inherits from the parent class house.
#Overridden __init__ Method: This method overrides the parent class's __init__ method.
#self.color = color + " color": Appends " color" to the color string and sets it as the instance attribute color.
#self.size = size + " BHK": Appends " BHK" to the size string and sets it as the instance attribute size.
#Overridden display Method: This method overrides the parent class's display method.
#print(f"Shreeya's house is {self.color} and she lives in {self.size}"): Prints a formatted string describing Shreeya's house.
        
myhouse = Shreeyahouse("red" , "5")
myhouse.display()

#myhouse = Shreeyahouse("red", "5"): Creates an instance of the Shreeyahouse class with color set to "red" and size set to "5".
#The __init__ method of Shreeyahouse modifies these values to "red color" and "5 BHK".
#myhouse.display(): Calls the overridden display method, which prints "Shreeya's house is red color and she lives in 5 BHK".

h = house("white" , "4")
h.display()

#h = house("white", "4"): Creates an instance of the house class with color set to "white" and size set to "4".
#h.display(): Calls the display method of the house class, which does nothing because the method is not implemented in the parent class.
        