print('Kupujemy komputer!!!')
miesiace = int( input('Ile miesięcy chcesz oszczędzać? ') )
konto = 0
cena_komputera = 5000

#pętla / instrukcja interacyjna
for i in range(miesiace):
    kwota = int( input('Ile wpłacasz w tym miesiącu: ') )
    konto = konto + kwota
    #konto += kwota

print(f"Zebrałeś {konto} zł")
if konto >= cena_komputera:
    print("Brawo, idziemy po komputer")
else:
    print(f"Brakuje cie jeszcze {cena_komputera - konto} zł")

print("-" * 50)