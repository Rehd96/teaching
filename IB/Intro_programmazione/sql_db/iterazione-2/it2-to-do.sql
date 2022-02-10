/* 1. Rendere l'attributo 'id' della relazione "ordine" una chiave primaria */ 
ALTER TABLE public.ordine ADD PRIMARY KEY (id);

/* 2. Rendere il attributo 'id' della relazione "ordine" come autoincrementante */
ALTER TABLE IF EXISTS public.ordine ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;


/* 3. Crare una relazione "menu" con i seguenti campi: 
        - id --> numerico 
        - nome_pizza --> text 
        - prezzo --> text 
        - pizza_bianca --> numerico (1 oppure 0)
        */
CREATE TABLE "menu" (id INTEGER NOT NULL,nome_pizza varchar(15),prezzo decimal,pizza_bianca boolean);


/* 4. Rendere l'attributo id della relazione "menu" una chiave primaria autoincrementante */ 
ALTER TABLE public.menu ADD PRIMARY KEY (id);



/* 5. Elimina tutti i dati dalla relazione "ordine" */



/* 6. Modificare la relazione "ordine" nel seguente modo: 
        6.1 Eliminare l'attributo "nome_pizza"
        6.2 Aggiungere l'attributo "id_pizza" 
        6.3 Rendere "id_pizza" una chiave esterna verso la chiave primaria della relazione "ordine" */  
ALTER TABLE public.ordine DROP COLUMN nome_pizza;
ALTER TABLE public.ordine ADD COLUMN id_pizza integer;
ALTER TABLE public.ordine ADD CONSTRAINT fk_menu FOREIGN KEY (id_pizza) REFERENCES public.menu (id) 


/* 7. Aggiungere i seguenti vincoli sulle relazioni: 
    7.1 Vincolo 'check' sull'attributo "pizza_bianca" per controllare se il valore inserito è 0 oppure 1 
    7.2 Vincolo 'check' sull'attributo "prezzo" per controllare se il valore inserito è maggiore di 0
    7.3 Vincolo 'unique' sull'attributo "nome_pizza" della relazione "menu"
    7.4 Default su attributo "totale_ordine" pari a 0.00 */

ALTER TABLE menu ADD CONSTRAINT check_quantita_maggiore_zero CHECK (menu.prezzo > 0); 
ALTER TABLE menu ADD CONSTRAINT unique_nome_pizza UNIQUE (nome_pizza); 
ALTER TABLE ordine ALTER COLUMN totale_ordine SET DEFAULT 0.00;




/* 8. Inserisci a tuo piacimento 5 record nella relazione "menu" e 10 record nella relazione "ordine" */
