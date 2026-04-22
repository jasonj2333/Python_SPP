koszt_komputera = 9000
konto = 0

while konto < koszt_komputera:
    wplata = int(input("Podaj wysokość wpłaty: "))
    if wplata > 0:
        konto += wplata
        #konto = konto + wplata
    print(f"Stan konta: {konto} zł")

print(f"Idziemy po komputer")