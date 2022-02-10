from soluzione_it5.cliente import Cliente
from soluzione_it5.banca import Banca
from soluzione_it5.conto import Conto
from soluzione_it5.conto import ContoSpecial
from soluzione_it5.persistence import PersistenceHanlder

relative_path = 'bank_managment_system_pro/it_5/soluzione_it5/data/data.json'

# CODICE DI TEST. Rispondi alle domande scritte nei commenti #
cliente1 = Cliente('Davide', '3924663077')
cliente2 = Cliente('Simona', '3335688985')
cliente3 = Cliente('Marco', '3335688285')

banca_san_paolo = Banca('Banca San Paolo')
banca_fineco = Banca('Banca San Paolo', 'GE')




conto1 = ContoSpecial(1587,cliente1)
conto2 = ContoSpecial(1588,cliente1)
conto3 = ContoSpecial(1685,cliente2)
conto4 = ContoSpecial(1987,cliente3)

banca_san_paolo.aggiungi_cliente(cliente1)
banca_san_paolo.aggiungi_cliente(cliente2)
banca_san_paolo.aggiungi_cliente(cliente3)
banca_san_paolo.apri_conto_corrente(conto1)
banca_san_paolo.apri_conto_corrente(conto2)
banca_san_paolo.apri_conto_corrente(conto3)
banca_san_paolo.apri_conto_corrente(conto4)

conto1.versa_soldi(500)


# Persistenza 
lista_banche = []
lista_banche.append(banca_san_paolo)
lista_banche.append(banca_fineco)

lista_conto = []
lista_conto.append(conto1)
lista_conto.append(conto2)
lista_conto.append(conto3)
lista_conto.append(conto4)

lista_clienti = []
lista_clienti.append(cliente1)
lista_clienti.append(cliente2)
lista_clienti.append(cliente3)


persistenceHanlder = PersistenceHanlder()
persistenceHanlder.salva_banca(lista_banche)
persistenceHanlder.salva_conto(lista_conto)
persistenceHanlder.salva_cliente(lista_clienti)
