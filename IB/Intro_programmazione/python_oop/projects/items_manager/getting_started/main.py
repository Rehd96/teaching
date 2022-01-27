# Come definire una classe
class Item:
    def calculate_total_price(self, x, y):
        return x * y

# Come creare una istanza della classe
item1 = Item()

# come assegnare un attributo a quella classe
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# Chiamata ai metodi di quella particolare istanza:
print(item1.calculate_total_price(item1.price, item1.quantity))

# Come creare una istanza della classe (Ne possiamo creare quante ne vogliamo)
item2 = Item()

# Assegnare gli attributi
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# Chiamata ai metodi di quella particolare istanza:
print(item2.calculate_total_price(item2.price, item2.quantity))