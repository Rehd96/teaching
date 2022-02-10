from soluzione_it4.cliente import Cliente
from soluzione_it4.banca import Banca
from soluzione_it4.conto import Conto
from soluzione_it4.conto import ContoSpecial

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
print('saldo: ' + str(conto1.saldo)) 
print(conto1.preleva_soldi(498.5)) 


# RISPONDI ALLE DOMANDE SCRITTE NEI COMMENTI * 

#1. SCRIVI OUTPUT PREVISTO:  
conto1.versa_soldi(500)
print('saldo: ' + str(conto1.saldo)) 


#2. SCRIVI OUTPUT PREVISTO:
conto1.preleva_soldi(1500)
print('saldo: ' + str(conto1.saldo)) 


#3. SCRIVI OUTPUT PREVISTO:
conto1.preleva_soldi(150)
print('saldo: ' + str(conto1.saldo)) 


#3. SCRIVI OUTPUT PREVISTO:
conto1.versa_soldi(5000)
print('saldo: ' + str(conto1.saldo)) 



#5. SCRIVI OUTPUT PREVISTO:
print(banca_fineco.nazione) 



#6. SCRIVI OUTPUT PREVISTO: 
banca_fineco.nazione = 'SP'
print(banca_fineco) 



#7. SCRIVI OUTPUT PREVISTO:
#print(banca_fineco.__nazione) 