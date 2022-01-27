
'''
- "self" rappresenta l'istanza della classe. 
- Usando la parola chiave "self" possiamo accedere agli attributi e ai metodi della classe in python.
- Python esegue metodi in modo che l'istanza a cui appartiene il metodo, venga passata automaticamente. 
- Il primo parametro nella firma dei metodi è l'istanza stessa 
- "self" è sempre un puntamento all'oggetto corrente.
'''

#ESEMPIO 1: obj e self sono chiaramente la stessa cosa
class check:
    def __init__(self):
        print("Address of self = ", id(self))
 
obj = check()
print("Address of class object = ", id(obj))


# ESEMPIO 2:"self" è sempre il primo argomento che viene passato nel costruttore e 
# nel metodo di instanza (altrimenti, causa un errore)
class car():    
    # Costruttore
    def __init__(self, model, color):
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
# Entrambi gli oggetti hanno differenti "self" che contengono i propri attributi
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")
 
audi.show()     # stesso output di car.show(audi)
ferrari.show()  # stesso output di car.show(ferrari)


# ESEMPIO 3: "self" è sempre richiesto come primo argomento
class check:
    def __init__():
        print("This is Constructor")
 
object = check()
print("Worked fine")

# ESEMPIO 4: "self" è una convezione, non una keyword
class this_is_class:
    def __init__(in_place_of_self):
        print("Abbiamo usato una parola diversa da self")
         
object = this_is_class()