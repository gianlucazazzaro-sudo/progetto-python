print("saldo = 1000")
saldo = 1000
while True :
    print("\n" * 20)
    print("\n---------------------------------------------------")
    print("Benvenuto nel simulatore di bancomat")
    print("---------------------------------------------------")
    print("1 controlla saldo")
    print("2 Deposita")
    print("3 preleva")
    print("4 esci")
    print("---------------------------------------------------")
    scelta = input("scegli un opzione: ")
    if scelta == "1" :
        print("il tuo saldo è: " + str(saldo))
        input("premi invio per continuare...")
    if scelta == "2":
        try:
            deposito= input("quanto vuoi depositare: ")
            print("hai depositato: " + deposito)
            saldo += int(deposito)
            print("il tuo saldo è: " + str(saldo))
            input("premi invio per continuare...")
        except ValueError:
            print("errore: inserisci un numero valido")    
            input("premi invio per continuare...")
               
    if scelta == "3":
        prelievo= input("quanto vuoi prelevare: ")
        try:
            if int(prelievo) > saldo:
                print("errore: non hai abbastanza soldi")
                input("premi invio per continuare...")
                continue
           
            print("hai prelevato: " + prelievo)
            saldo -= int(prelievo)
            print("il tuo saldo è: " + str(saldo))
            input("premi invio per continuare...")
        except ValueError:
            print("errore: inserisci un numero valido")
            input("premi invio per continuare...")
    if scelta == "4":
        print("uscita in corso...")
        break
