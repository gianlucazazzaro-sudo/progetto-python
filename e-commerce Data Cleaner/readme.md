# E-commerce Data Cleaner & Reporter

Un'applicazione Python per l'automazione aziendale che trasforma i log grezzi e disordinati delle vendite di un e-commerce in un report di spesa clienti pulito, aggregato e ordinato.

## 🚀 Funzionalità
- **Gestione Errori:** Controllo sicuro sull'apertura del file con gestione delle eccezioni.
- **Data Cleaning:** Filtraggio automatico delle sole righe di acquisto ed eliminazione dei dati di sola visita.
- **Parsing Avanzato:** Estrazione e formattazione dei nomi dei clienti (rimozione caratteri speciali e formattazione Capital Case) e conversione dei prezzi in formato numerico `float`.
- **Classifica Top Spenders:** Aggregazione dei dati tramite dizionari e ordinamento decrescente (dal cliente che ha speso di più a quello che ha speso di meno) tramite tuple.

## 📂 Struttura del file di input atteso (`.txt`)
Il programma analizza file di log strutturati in questo modo:
`ORDINE - Cliente: carlo_verdi - Prodotto: Giacca - Prezzo: 120.00 EUR`
`VISITA - Cliente: sara_f - Prodotto: Scarpe`

## 🛠️ Tecnologie utilizzate
- Python 3
- Strutture dati: Liste, Dizionari, Tuple (Stile *Python for Everybody* avanzato)