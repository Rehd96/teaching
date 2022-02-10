'''
L'ereditarietà è un meccanismo grazie al quale una classe derivata (o child class) può acquisire le funzionalità definite in una classe base 
(o parent class) senza dover operare alcune modifica a carico di quest'ultima. 

L'utilizzo dell'ereditarietà presenta principalmente un vantaggio: consente di non dover riscrivere codice già digitato rendendolo riutilizzabile.
'''

class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome--> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")


class Studente(Persona):
    pass

class Insegnante(Persona):
    pass


p = Persona('Davide', 'Fella', '25', 'Strada acquedotto')
print(p.scheda_personale()) 

s = Studente('Davide', 'Fella', '25', 'Strada')
print(s.scheda_personale()) 

help(s)


'''
- Prossimo step personalizziamo le classe figlie, aggiungendo informazioni 
'''
class Studente(Persona):
    profilo = "Studente"

    def __init__(self,nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso di Studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda
    
    def cambio_corso(self,corso):
        self.corso_di_studio = corso
        print(f"Corso Aggiornato")


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self,nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Materie Insegnate:{self.materie}
        ***"""
        return super().scheda_personale() + scheda
    
    def aggiungi_materia(self,nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco Aggiornato")


p2 = Persona('Davide', 'Fella', '25', 'Strada acquedotto')
print(p.scheda_personale()) 

s2 = Studente('Davide', 'Fella', '25', 'Strada')
print(s.scheda_personale()) 