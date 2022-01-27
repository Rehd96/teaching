--1. Creare un database con Postgresql chiamato "pizzeria_da_luigi" utilizzando PgAdmin (o un client a tua scelta)
 
--2 All'interno del database crea una una tabella "ordine"
CREATE TABLE "ordine" (id INTEGER NOT NULL, nome_pizza varchar(15), nome_cliente varchar(30), data_ordine timestamp, totale_ordine decimal)

--3 Popolare la tabella
INSERT INTO "ordine" VALUES(0, 'Margherita', 'Davide', '14/01/2022 20:05', 5.5); 
INSERT INTO "ordine" VALUES(1, 'Peperoni', 'Davide', '14/01/2022 20:05', 7); 
INSERT INTO "ordine" VALUES(2, 'Margherita', 'Marco', '14/01/2022 21:05', 5.5); 
INSERT INTO "ordine" VALUES(3, '4 Formaggi', 'Carla', '15/01/2022 20:05', 8); 
INSERT INTO "ordine" VALUES(4, 'Diavola', 'Marta', '16/01/2022 19:05', 7.5);
INSERT INTO "ordine" VALUES(5, 'Diavola', 'Marta', '16/01/2022 19:06', 7.5);
INSERT INTO "ordine" VALUES(6, 'Margherita', 'Davide', '17/01/2022 22:00', 5.5);
INSERT INTO "ordine" VALUES(7, 'Boscaiola', 'Anna', '17/01/2022 22:10', 8.5);
INSERT INTO "ordine" VALUES(8, 'Margherita', 'Marco', '17/01/2022 21:00', 5.5);
INSERT INTO "ordine" VALUES(9, 'Margherita', 'Simona', '17/01/2022 20:30', 5.5);


/*
INSERT INTO "ordine" VALUES(0, 'Margherita', 'Davide', '2022-01-01 21:05', 5.5); 
INSERT INTO "ordine" VALUES(1, 'Peperoni', 'Davide', '2022-01-01 22:00', 7); 
INSERT INTO "ordine" VALUES(2, 'Margherita', 'Marco', '2022-01-01 22:05', 5.5); 
INSERT INTO "ordine" VALUES(3, '4 Formaggi', 'Carla', '2022-01-03 19:15', 8); 
INSERT INTO "ordine" VALUES(4, 'Diavola', 'Marta', '2022-01-03 19:45', 7.5);
INSERT INTO "ordine" VALUES(5, 'Diavola', 'Marta', '2022-01-03 20:06', 7.5);
INSERT INTO "ordine" VALUES(6, 'Margherita', 'Davide', '2022-01-05 20:10', 5.5);
INSERT INTO "ordine" VALUES(7, 'Boscaiola', 'Anna', '2022-01-05 20:10', 8.5);
INSERT INTO "ordine" VALUES(8, 'Margherita', 'Marco', '2022-01-07 21:00', 5.5);
INSERT INTO "ordine" VALUES(9, 'Margherita', 'Simona', '2022-01-07 20:30', 5.5); */

--4 Tutte le colonne dalla tabella "ordine" senza ordinamento o selezioni 
SELECT * FROM "ordine"

--5 Solamente le colonne "id", "totale_ordine", "data_ordine"
SELECT id, totale_ordine, data_ordine FROM "ordine"

--6 Tutti i clienti presenti nella tabella ma senza ripetizioni dei record
SELECT DISTINCT nome_cliente from "ordine"

--7 Le pizze ordinate da uno specifico cliente
SELECT * FROM "ordine" WHERE nome_cliente = 'Davide'

--8 Le pizze ordinate in una specifica data
SELECT * FROM "ordine" WHERE data_ordine BETWEEN '15/01/2022 00:00' AND '16/01/2022 00:00'

--9 Le righe che hanno come nome della pizza "margherita" e come cliente "Davide"
SELECT * FROM "ordine" WHERE nome_pizza = 'Margherita' AND nome_cliente = 'Davide'

--10 Contare quante righe sono presenti nella tabella
SELECT COUNT(*) FROM "ordine"

--11 Gli ordini che sono di uno specifico giorno
SELECT * FROM "ordine" WHERE data_ordine BETWEEN '15/01/2022 00:00' AND '16/01/2022 00:00'

--12 Selezionare gli ordini con 3 nomi diversi di pizza (Utilizzare costrutto IN)
SELECT * FROM "ordine" WHERE nome_pizza IN ('Margherita', 'Boscaiola', 'Diavola')

--13 Il totale dei prezzi 
SELECT SUM(totale_ordine) AS "Totale ordini" FROM "ordine" 

--14 Il totale dei prezzi per una singola giornata
SELECT SUM(totale_ordine) AS "Totale ordini" FROM "ordine"  WHERE data_ordine BETWEEN '15/01/2022 00:00' AND '16/01/2022 00:00'

--15 La media dell'incasso giornalieria 
SELECT AVG(totale_ordine) AS "Media incasso giornaliera" FROM "ordine"

--16 Il minimo ordine di ogni cliente 
SELECT nome_cliente, MAX(totale_ordine)  FROM "ordine" group by nome_cliente

--17 Tutti i giorni in cui c'è stato almeno un ordine (solo data no ora e minuti)
SELECT distinct date(data_ordine) from "ordine"

--18 Tutti gli ordini a più di 6 euro e meno di 8
SELECT * FROM "ordine" where totale_ordine > 6 and totale_ordine < 8

--19
select * from "ordine"  order by "ordine".data_ordine DESC limit 5
