print("parcheggio a pagamento")
print("tariffa auto 3.00 € a ora, tariffa moto 1.50 € a ora ")
print("maxisosta : più di 10 ore sconto 20% ore successive ")
try:
    veic=input("tipo di veicolo : auto A moto M : ").upper()
    if veic=="A" or veic=="M" :

        ora_sosta=float(input("tempo di sosta : "))
        if veic == "A" :
        
            if 0 < ora_sosta <= 10 :
                prezzo=ora_sosta*3
                print(f"il costo della sosta è : {prezzo:.2f} ")
           
            elif ora_sosta > 10 :
                prezzo_base_auto=10*3
                ore_extra=ora_sosta-10
                sconto_auto=ore_extra*3*0.8
                maxi_sosta=prezzo_base_auto+sconto_auto
                print(f"costo parcheggio : {maxi_sosta:.2f}")

        elif veic =="M" :
            if 0 < ora_sosta <= 10 :
                prezzo=ora_sosta*1.50
                print(f"il costo della sosta è : {prezzo:.2f} ")

            elif ora_sosta > 10 :
                prezzo_base_moto=10*1.50
                ore_extra=ora_sosta-10
                sconto_moto=ore_extra*1.50*0.8
                maxi_sosta=prezzo_base_moto+sconto_moto
                print(f"costo parcheggio : {maxi_sosta:.2f}")
    else:
        print("veicolo non riconosciuto ")
except ValueError:
    print("inserisci un valore corretto")
    
        



