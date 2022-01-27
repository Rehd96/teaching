'''
1. Cosa sono i getter e setter

- Getter, utilizzati per accedere agli attributi privati da una classe.
- Setter: utilizzati per impostare il valore su attributi privati in una classe.

Sono spesso utilizzati in Python quando: 
    - Vogliamo aggiungere una validazione logica intorno ad un get o set di un valore
    - Per evitare di accedere direttamente ad un field di una classe, quando ad esempio un valore 
    non è accessibile direttamente 
'''

'''
2. Vediamo come implementare un attributo privato in una classe. Nel seguente esempio la classe ha 3 metodi. 
+ __init__  --> Usata per inizializzare gli attributi o le propietà di una classe
+ __a       --> Attributo privato 
+ get_a     --> per leggere i valori di un attributo privato 
+ set_a     --> usato per settare i valori di a

Nota: non puoi accedere ad una variabile privata direttamente in Python, per questo implementiamo i 
metodi getter

In questa classe stiamo nascondendo gli attributi privati e i metodi. Stiamo implementando quella che 
si chiama "Encapsulation" della OOPS. 
'''
class SampleClass:

    def __init__(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a


## crea l'oggetto
obj = SampleClass(10)

## prendi il valore di 'a' usanto il getter
print(obj.get_a())

## setta il nuovo valore di 'a' usando obj
obj.set_a(45)

print(obj.get_a())


''''
3. Property 

E se volessimo aggiungere una logica sul set dei dati? 

@property è usato per prendere il valore di un attributo senza usare il metodo getter. 

Per fare il set di una variabile, utilizziamo il decorator @method_name.setter di fronte il metodo. 
@a.setter setta il valore di 'a' controllando le condizioni menzionate nel metodo. 
'''

class Property:

    def __init__(self, var):
        ## initializing the attribute
        self.a = var

    @property
    def a(self):
        return self.__a

    ## the attribute name and the method name must be same which is used to set the value for the attribute
    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2


## creating an object for the class 'Property'
obj = Property(23)

print(obj.a)


'''
Vediamo un altro modo di utilizare la funzione property
'''
class FinalClass:

    def __init__(self, var):
        self.__set_a(var)

    def __get_a(self):
        return self.__a

    def __set_a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

    a = property(__get_a, __set_a)

obj = FinalClass(132)

print(obj.a)