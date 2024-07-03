class Jeep:
    def __init__(self):
        self.paint_colour = "blue"
    
    @staticmethod
    def gear_systems():
        Jeep.gear_system = "automatic"

j = Jeep()
k = Jeep()
j.paint_colour = "red"
k.paint_colour = "green"
Jeep.gear_systems()
print(j.paint_colour)
print(j.gear_system)
j.gear_system = "manual"
print(k.paint_colour)
print(k.gear_system)   




#create a class Jeep
#create an instance variable called paint_colour
#create 2 instances and change the colour of both the instances
#create static variable called gear_system
#create 2 instances and change the gear_system from automatic to manual using 1 instance
#check whether it is changed for all the instances. 