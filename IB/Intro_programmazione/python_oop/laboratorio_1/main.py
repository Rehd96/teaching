# How to create a class:
class Item:
    name = ''
    price = ''
    quantity = ''
    
      
    def __init__(self,name=0,price=0,quantity=0):
        self.name = name
        if price < 0 :
            raise ValueError("price non può essere minore di 0 ")
        self.price = price
        if quantity < 0:
            raise ValueError("quantity non può essere minore di 0")
        self.quantity = quantity
        
    
        
    def calculate_total_price(self):
        return self.price * self.quantity

# How to create an instance of a class
item1 = Item("Phone",100,5)

# Calling methods from instances of a class:
print(item1.calculate_total_price())

# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item("laptop",1000,3)


# Calling methods from instances of a class: 
print(item2.calculate_total_price())