class Conto:
    def __init__(self, numero_conto, cliente, saldo=0.00):
        self.numero_conto = numero_conto
        self.cliente = cliente
        self.saldo = saldo

    def __repr__(self):
        return "Conto " + self.numero_conto + " intestato a cliente " + self.cliente.nome_cliente  + " con saldo " + str(self.saldo) + "€"