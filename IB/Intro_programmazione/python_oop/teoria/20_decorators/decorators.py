'''
Queste che seguono sono alcune nozioni utili che vale la pena ricorda per capire i decorator: 

- In python possiamo definire funzioni dentro altre funzioni
- In Python una funzione può essere passata come parametro ad un'altra funzione (e ritornata)
'''

#ESEMPIO 1: aggiungiamo un messaggio di benvenuto alla stringa
def messageWithWelcome(str):
  
    # funzione annidata
    def addWelcome():
        return "Welcome to "
  
    # Ritorna una concatenazione di addWelcome e di una stringa
    return addWelcome() + str
  
def message(msg):
    return msg
  
print( messageWithWelcome(message("Hello World!")) ) 


'''
- Un decorator è una funzione che accetta una funzione come unico parametro e restituisce una 
funzione
- Questo è utile per fare fare un 'wrap' intorno alla funzionalità con lo stesso codice 
più e più volte

Ad esempio, il codice sopra può essere riscritto come segue, usiamo @func_name 
per specificare un decoratore da applicare su un'altra funzione.
'''

# Aggiunge un messaggio di benvenuto alla stringa tornata da fun(). Prende la funzione 
# fun() come parametro e torna welcome()
def decorate_welcome_message(fun):
  
    # Funzione annidata
    def addWelcome(msg):
        return "Welcome to " + fun(msg)
  
    # Decorator torna una funzione 
    return addWelcome
  
@decorate_welcome_message
def message(message_to_print):
    return message_to_print;
  
a = message("Message with decorator")
print( a ) 


#ESEMPIO 2: Decorator che logga data e time quando una funzione viene eseguita
from datetime import datetime
def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        func()
    return wrapper

@log_datetime
def daily_backup():
    print('Daily backup job has finished.')   
     
daily_backup()