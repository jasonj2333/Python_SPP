koszt_komputera = 8000
konto = 0

miesiace = ["styczniu", "lutym", "marcu", "kwietniu", "maju", "czerwcu", "lipcu", "sierpniu", "wrześniu", "październiku", "listopadzie", "grudniu"]

for miesiac in miesiace:
#for miesiac in range(1, 12+1):
    wplata = int( input(f"Podaj wysokość wpłaty w {miesiac}: ") )
    konto = konto + wplata

print(f"Stan konta wynosi: {konto} zł")

if(konto >= koszt_komputera):
    print("Idziemy kupić komputer")
else:
    print(f"Brakuje ci jeszcze {koszt_komputera - konto} zł")