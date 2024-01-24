print("Kupujemy komputer")
cena_komputera = float( input("Podaj cenę komputera: ") )
konto = 0

while cena_komputera > konto:
    wplata = float( input("Ile chcesz wpłacić? ") )
    konto += wplata
    print(f"Stan konta: {konto:.2f}")

print("Brawo, zebrałeś pieniądze na komputer")
