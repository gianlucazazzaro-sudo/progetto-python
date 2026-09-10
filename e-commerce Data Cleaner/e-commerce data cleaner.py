nome_file=input("Inserisci il file da analizzare: ")
try:
    fname=open(nome_file)
except FileNotFoundError:
    print("File non trovato")
    exit()
dati_ut=dict()
ordini_ut=dict()
for riga in fname :
    riga=riga.strip()
    
    if "ORDINE" in riga:
        riga_pulita=riga.split("-")
        nome_cliente=riga_pulita[1].split(":")
        nome_cliente=nome_cliente[1].strip()
        nome_cliente=nome_cliente.replace("_"," ").title()
        pezzi_prezzo = riga_pulita[-1].split(":")
        cifra_prezzo = pezzi_prezzo[1].split()
        prezzo = float(cifra_prezzo[0])
        dati_ut[nome_cliente]=dati_ut.get(nome_cliente,0.0)+prezzo
        ordini_ut[nome_cliente]=ordini_ut.get(nome_cliente,0)+1
print(dati_ut)
print(ordini_ut)

lista_ordinata=list()
fatturato_totale=0

for chiave,valore in dati_ut.items():
    n_ordini=ordini_ut[chiave]
    media_cliente=valore/n_ordini
    fatturato_totale+=valore
    n_tupla=(valore,chiave,n_ordini,media_cliente)
    lista_ordinata.append(n_tupla)

print("fatturato totale: ",fatturato_totale)
spesa_media=fatturato_totale/len(lista_ordinata)
print("La spesa media per cliente è: ",spesa_media)
 

lista_ordinata.sort(key=lambda x:x[2], reverse=True)


print("\n--- REPORT FINALE SPESE CLIENTI ---")
for valore,chiave,n_ordini,media_cliente in lista_ordinata:
    print(f"Cliente: {chiave:<20} | Ordini: {n_ordini:<3} | Spesa Totale: {valore:<8.2f} EUR | Media: {media_cliente:2f}")


import pandas as pd

df=pd.DataFrame(lista_ordinata,columns=["Spesa Totale (EUR)","Cliente","Numero Ordini","Spesa Media (EUR)"])
df=df[["Cliente", "Numero Ordini", "Spesa Totale (EUR)", "Spesa Media (EUR)"]]
df_sommario = pd.DataFrame({
    "Metrica": ["Fatturato Totale", "Spesa Media per Cliente", "Numero Clienti Totali"],
    "Valore": [fatturato_totale, spesa_media, len(lista_ordinata)]})


with pd.ExcelWriter("report_spese_clienti.xlsx", engine="openpyxl") as writer:
    df_sommario.to_excel(writer, sheet_name="Sommario", index=False)
    df.to_excel(writer, sheet_name="Classifica Clienti", index=False)

print("\n[OK] File Excel 'report_spese_clienti.xlsx' aggiornato con due fogli!")


df.to_csv("report_spese_clienti.csv", index=False, sep=";")
print("[OK] File CSV 'report_spese_clienti.csv' creato con successo!")



    
        