'''
- @classmethod è una funzione built-in decorator di Python, è una espressione che viene 
valutata dopo la definizione della tua funzione di classe. Un metodo di classe riceve
la classe come primo argomento implicito ('cls' per convenzione). 

class C: 
    @classmethod
    def myFunction(cls, arg1, arg2, arg3...)
        my code 
        
Dove myFunction è la mia funzione da convertire in un metodo di classe ritorna un metodo di classe per una funzione 
Un metodo di classe è un metodo che è legato alla classe (e poi modificarne lo stato) e non all'istanza



- @staticmethod non riceve in maniera implicita nessum argomento 

class C:
    @staticmethod
    def myFunction(arg1, arg2, ...):
        my code
 
Un metodo statico non può modoficare lo stato di una classe o accedervi, è presente in una classe
perché a livello logico può avere senso.
In generale, possiamo vedere un metodo statico come una utiliy che può servire in più punti del codice

Generalmente utilizziamo un metodo di classe per creare metodi 'factory' mentre utilizziamo metodi 
statici quando vogliamo creare delle utility che non hanno però bisogno di accedere allo stato 
di quella particolare classe. 

'''

@staticmethod
def is_integer(num): 
    try: 
        int(num); 
        return True; 
    except ValueError: 
        return False

@classmethod
def instantiate_from_csv(cls):
    csv_path = 'IB\Intro_programmazione\python_oop\projects\items_manager\iterazione-2.1\extra_exercises\items.csv'

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)  
        items = list(reader)

        for item in items:
            if cls.is_integer(item.get('quantity')): 
                pass 
