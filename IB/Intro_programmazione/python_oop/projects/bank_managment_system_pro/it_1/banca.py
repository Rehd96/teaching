class Banca: 
    def __init__(self, nome_banca): 
        self.nome_banca = nome_banca
        self.clienti = []
        self.conti_correnti = []

    def __repr__(self):
        return "Nome banca " + self.nome_banca + " numero totale di clienti " + str(len(self.clienti)) + " numero totale di conti correnti: " + str(len(self.conti_correnti))  