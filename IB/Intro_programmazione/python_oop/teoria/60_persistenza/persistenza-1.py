import os
relative_path = 'IB/Intro_programmazione/python_oop/teoria/60_persistenza/demo_file.json'

def salva_su_file(): 
    print('** Salvo file **')

    f = open(relative_path, "a")
    f.write("Yee un'altra riga aggiuntiva!")
    f.close()

def leggi_da_file(): 
    print('** Leggo file **')

    f = open(relative_path, "r")
    print(f.read())

def sovrascrivi_file(): 
    print('** Sovrascrivi file **')

    f = open(relative_path, "w")
    f.write("Abbiamo sovrascritto il contenuto")
    f.close()

def rimuovi_file(): 
    print('** Rimuovo file **')
    
    os.remove(relative_path)

salva_su_file()
leggi_da_file()
sovrascrivi_file()
rimuovi_file()
