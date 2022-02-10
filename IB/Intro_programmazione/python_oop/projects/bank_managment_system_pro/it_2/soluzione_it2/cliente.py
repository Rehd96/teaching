class Cliente: 
    def __init__(self, nome_cliente, numero_telefono):
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono

    # Definizione di getter e setter #
    @property
    def nome_cliente(self): 
        return self.__nome_cliente
    
    @nome_cliente.setter
    def nome_cliente(self, nome_cliente): 
        self.__nome_cliente = nome_cliente

    @property
    def numero_telefono(self): 
        return self.__numero_telefono

    @numero_telefono.setter
    def numero_telefono(self, numero_telefono): 
        self.__numero_telefono = numero_telefono

    def __repr__(self):
        return "Cliente " + self.nome_cliente + " telefono " + self.numero_telefono