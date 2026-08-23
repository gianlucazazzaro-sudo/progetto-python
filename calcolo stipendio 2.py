def calcola_stip(ore_lav,tariffa):
    if ore_lav <=40:
        stip=ore_lav*tariffa
    else:
        stip=40*tariffa+(ore_lav-40)*tariffa*1.5
    return stip

while True:
    try:
        ore_lav=float(input("Quante ore hai lavorato ? "))
        paga_oraria=float(input("Quanto prendi a ore ? "))
    except ValueError:
        print("Errore: inserisci un numero valido.")
        continue

    stipendio=calcola_stip(ore_lav,paga_oraria)
    print("Il tuo stipendio è :",stipendio)
   
    while True:
        scelta = input("Vuoi continuare? (s/n): ").lower().strip()
        
        if scelta == "s" or scelta == "n":
            break # Esce da QUESTO ciclo interno perché la risposta è valida
        else:
            print("Risposta non valida! Inserisci solo 's' per sì o 'n' per no.")

    # Ora controlliamo il valore della scelta valida
    if scelta == "n":
        print("Arrivederci!")
        break 
    



