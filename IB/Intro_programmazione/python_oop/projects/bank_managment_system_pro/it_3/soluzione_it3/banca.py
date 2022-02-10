from soluzione_it3.utility import Utility

class Banca: 
    def __init__(self, nome_banca): 
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []
        self.__id = id(self)
        print(f'Istanza banca creata con id: {self.__id}')

    # Definizione di getter e setter #
    @property
    def id(self): 
        return self.__id

    @property
    def nome_banca(self): 
        return self.__nome_banca

    @nome_banca.setter
    def numero_telefono(self, nome_banca): 
        self.__nome_banca = nome_banca

    @property
    def clienti(self): 
        return self.__clienti

    @clienti.setter
    def clienti(self, clienti): 
        self.__clienti = clienti

    @property
    def conti_correnti(self): 
        return self.__conti_correnti

    @conti_correnti.setter
    def numero_telefono(self, conti_correnti): 
        self.conti_correnti = conti_correnti

    def __repr__(self):
        return "Nome banca " + self.nome_banca + " numero totale di clienti " + str(len(self.clienti)) + " numero totale di conti correnti: " + str(len(self.conti_correnti))  

    def aggiungi_cliente(self, cliente): 
        self.clienti.append(cliente)
    
    def rimuovi_cliente(self, id): 
        assert Utility.is_integer(id), "Inserire un id intero"        
        assert int(id) > 0, "Inserire un id valido"
        
        pos=-1
        for index in range(0, len(self.clienti)): 
            if self.clienti[index].id == int(id):
                pos = index
                break
            
        if pos<0: 
            print("ERROR: id cliente non trovato")
        else: 
            self.clienti.pop(pos)
            print("cliente " + str(id) + " rimosso con successo")

    def apri_conto_corrente(self, conto): 
        self.conti_correnti.append(conto)
    
    def chiudi_conto_corrente(self, numero_conto): 
        assert Utility.is_integer(numero_conto), "Inserire un numero intero"        
        assert int(numero_conto) > 0, "Inserire un numero valido"
        
        pos=-1
        for index in range(0, len(self.conti_correnti)): 
            if self.conti_correnti[index].numero_conto == int(numero_conto):
                pos = index
                break
            
        if pos<0: 
            print("ERROR: numero conto non trovato")
        else: 
            self.conti_correnti.pop(pos)
            print("conto corrente numero " + str(numero_conto) + " rimosso con successo")
            