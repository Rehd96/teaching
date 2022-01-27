from soluzione_it1.cliente import Cliente
from soluzione_it1.banca import Banca
from soluzione_it1.conto import Conto

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

#1. OUTPUT PREVISTO:  
print( cliente1.nome_cliente )


#2. OUTPUT PREVISTO:  
print(account.cliente.nome_cliente) 


#3. OUTPUT PREVISTO: 
cliente1.nome_cliente = 'Giovanni'
print(account.cliente.nome_cliente) 

