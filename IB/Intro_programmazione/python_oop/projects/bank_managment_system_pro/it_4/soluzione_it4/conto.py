from datetime import datetime

class Conto:
    tassa_prelievo = 1.00

    def __init__(self, numero_conto, cliente, saldo=0):
        self.__numero_conto = numero_conto
        self.__cliente = cliente
        self.__saldo = saldo
        self.__id = id(self)
        print(f'Istanza conto creata con id: {self.__id}')

    # Definizione di getter e setter #
    @property
    def numero_conto(self): 
        return self.__numero_conto
    
    @numero_conto.setter
    def numero_conto(self, numero_conto): 
        self.__numero_conto = numero_conto

    @property
    def cliente(self): 
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente): 
        self.__cliente = cliente

    @property
    def saldo(self): 
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo): 
        self.__saldo = saldo

    def versa_soldi(self, value): 
        self.saldo += value
    
    def preleva_soldi(self, value): 
        if self.saldo < value + self.tassa_prelievo: 
            print('Importo richiesto non presente sul conto')
        else: 
            self.saldo -= value + self.tassa_prelievo
            print(f'Hai prelevato é {value}. Nuovo saldo del conto: {self.saldo}')

    def __repr__(self):
        return "Conto " + self.numero_conto + " intestato a cliente " + self.cliente.nome_cliente  + " con saldo " + str(self.saldo) + "€"

#
# ContoSpecial rappresenta un conto particolare, sono più alte le tasse di 
# prelievo ma posso andare in negativo
# #
class ContoSpecial(Conto): 
    tassa_prelievo = 2
    data_inizio_debito = None

    def __init__(self, numero_conto, cliente, data_inizio_debito, saldo=0):
        super.__init__(numero_conto, cliente, saldo)
        self.data_inizio_debito = data_inizio_debito
        print(f'Istanza conto creata con id: {self.__id}')


    def preleva_soldi(self, value): 
        self.saldo -= (value + self.tassa_prelievo)
        print(f'Hai prelevato é {value}. Nuovo saldo del conto: {self.saldo}')

        if self.saldo < 0 and self.data_inizio_debito == None: 
            self.data_inizio_debito = datetime.now()
            print(f'ATTENZIONE: Il tuo saldo è diventato negativo!')
  
    def versa_soldi(self, value):
        super().versa_soldi(value)

        if (self.saldo > 0 and self.data_inizio_debito != None):
            self.data_inizio_debito = None
            print('ATTENZIONE: Il  saldo è tornato positivo')
         