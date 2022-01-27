import csv

class Item:
    pay_rate = 0.8 #20% sconto
    all_items = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
       
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_items.append(self)
        
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return self.apply_discount(self.price) * self.quantity

    def apply_discount(self, price):
        return price * self.pay_rate

    # completare il corpo della funzione
    def is_integer(self, num): 
        try: 
            int(num); 
            return True; 
        except ValueError: 
            return False

    def instantiate_from_csv(self): 
        csv_path = 'IB\Intro_programmazione\python_oop\projects\items_manager\iterazione-2.1\extra_exercises\items.csv'

        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            if self.is_integer(item.get('quantity')): 
               Item(name=item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))

#Soluzione temporanea
item1 = Item('test', 5, 1)
item1.instantiate_from_csv()
print(Item.all_items)
