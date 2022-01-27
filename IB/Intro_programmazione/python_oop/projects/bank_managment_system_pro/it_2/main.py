from soluzione_it2.cliente import Cliente
from soluzione_it2.banca import Banca
from soluzione_it2.conto import Conto

# CODICE DI TEST. Rispondi alle domande scritte nei commenti #
cliente1 = Cliente('Davide', '3924663077')
cliente2 = Cliente('Simona', '3335688985')
cliente3 = Cliente('Marco', '3335688285')
banca_san_paolo = Banca('Banca San Paolo')
account = Conto('00001',cliente1)


# Per questi print mi aspetto la stampa nel metodo __repr__
print(account)
print(banca_san_paolo)
print(cliente1)


# RISPONDI ALLE DOMANDE SCRITTE NEI COMMENTI * 

#1. Commenta il metodo con il decorator @property nella classe Cliente per l'attributo nome_cliente. 
# OUTPUT PREVISTO:  
print( cliente1.nome_cliente )


#2. Decommenta il codice del punto #1. Ora cambia il nome del metodo con il decorator @property
# per l'attributo nome_cliente 
# OUTPUT PREVISTO:  
print(account.cliente.nome_cliente) 


#3. Commenta il metodo con decorator setter per l'attributo nome_cliente nella classe Ciente. 
# OUTPUT PREVISTO: 
cliente1.nome_cliente = 'Giovanni'
print(account.cliente.nome_cliente) 