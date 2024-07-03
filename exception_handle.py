#create a class called products
# create the necessary fields
# while calculating the total for the quantity , if the quantity is less than 5
# raise ValueError
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def total(self):
        if self.quantity < 5:
            raise ValueError
        

try:
    product1 = Product("Laptop", 3)
    print(product1.total())
except ValueError:
    print("Quantity less than 5")

    