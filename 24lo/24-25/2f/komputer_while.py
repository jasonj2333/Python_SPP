konto = 0
cena_komputera = 5000

while konto < cena_komputera:
    wplata = int(input("Podaj wysokość wpłaty: "))
    if wplata > 0:
        konto += wplata
    print(f"Stan konta {konto} zł")

print(f"Zebraleś {konto} zł")
print("Możesz kupić komputer")