kwota = int(input("Podaj cenę komputera: "))

suma_wplat = 0

while suma_wplat < kwota:
    wplata = int(input("Podaj wysokość wpłaty: "))
    suma_wplat = suma_wplat + wplata

print(f"Gratulacje, zebrałeś odpowiednią kwotę, masz: {suma_wplat}")