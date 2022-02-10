/* 1. Crea la relazione
 "cliente" con i seguenti attributi: 
    - id --> numerico non nullo, chiave primaria
    - nome --> text 
    - email --> text 
    - telefono --> text*/
CREATE TABLE cliente (id int PRIMARY KEY NOT NULL, 
					  nome TEXT, 
					  email TEXT, 
					  telefono TEXT); 


/* 2. Crea la relazione "riga_ordine" con i seguenti attributi: 
    - id --> numerico non nullo, chiave primaria
    - fk_ordine numero non nullo, chiave esterna verso "ordine" 
    - fk_riga_menu numerico non nulla, chiave esterna verso "menu"*/
CREATE TABLE riga_ordine (id int PRIMARY KEY NOT NULL, 
					  ordine_id int, 
					  riga_menu_id int);
ALTER TABLE riga_ordine ADD CONSTRAINT fk_ordine FOREIGN KEY (ordine_id) REFERENCES ordine(id);
ALTER TABLE riga_ordine ADD CONSTRAINT fk_riga_menu FOREIGN KEY (riga_menu_id) REFERENCES menu(id);


/* 3. Modificare la relazione  "ordine": 
    - Eliminare la colonna "nome_cliente"
    - Aggiungere una colonna fk_cliente di tipo integer, chiave esterna verso la relazione
     "cliente" */
ALTER TABLE ordine DROP COLUMN nome_cliente; 
ALTER TABLE ordine ADD COLUMN client_id int; 
ALTER TABLE ordine ADD CONSTRAINT fk_cliente FOREIGN KEY (client_id) REFERENCES cliente(id);



/* 4. Creare una relazione "tessera_punti" con i seguenti attributi: 
    - id --> numerico chiave primaria 
    - data_creazione --> timestamp
    - totale_punti --> numerico non nullo */
CREATE TABLE tessera_punti (id int PRIMARY KEY NOT NULL, 
					  data_creazione timestamp, 
					  totale_punti int);


/* 5. Creare una relazione "rider" con i seguenti attributi: 
    - id --> numerico, chiave primaria 
    - id_compagnia --> numerico, chiave esterna verso la tabella azienda_consegne*/
CREATE TABLE rider (id int PRIMARY KEY NOT NULL, 
					  id_compagnia int);
					  

/* 6. Creare una relazione "azienda_consegne": 
    - id --> mumerico, chiave primaria 
    - nome_azienda --> varchar
    - tariffa --> decimal*/
CREATE TABLE azienda_consegne (id int PRIMARY KEY NOT NULL, 
					  		   nome_azienda TEXT, 
							   tariffa decimal);

/* 7. Modificare la relazione "ordine" aggiugendo il seguente attributo: 
    - "id_rider", intero, chiave eserna verso l'id della relazione "azienda_consegne"*/
ALTER TABLE ordine ADD COLUMN id_rider int; 
ALTER TABLE ordine ADD CONSTRAINT fk_rider FOREIGN KEY (id_rider) REFERENCES rider(id);


ALTER TABLE rider ADD CONSTRAINT fk_azienda_consegne FOREIGN KEY (id_compagnia) REFERENCES azienda_consegne(id);



/* 8. Modificare la relazione "cliente": 
    - Creare un campo "id_tessera" e renderla chiave esterna verso la relazione "tessera punti" */
ALTER TABLE cliente ADD COLUMN id_tessera int; 
ALTER TABLE cliente ADD CONSTRAINT fk_cliente FOREIGN KEY (id_tessera) REFERENCES tessera_punti(id);

