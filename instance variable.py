class mouse:
    def __init__(self):
        self.no_of_buttons = 2
    
    def display(self):
        self.manufacturer = "zebronics"
    
    m = mouse()
    m.type = "wireless mouse"
    mse = mouse()
    print(mse.no_of_buttons)
    print(mse.manufacturer)
    print(mse.type)
