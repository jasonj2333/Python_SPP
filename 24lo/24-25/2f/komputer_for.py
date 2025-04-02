konto = 0
cena_komputera = 5000

#for miesiac in [1,2,3,4,5,6,7,8,9,10,11,12]:
for miesiac in range(1,12+1):
    wplata = input(f"{miesiac}. Podaj wysokość wpłaty: ")
    konto += int(wplata)

print(f"Zebrałeś {konto} złotych.")
if konto - cena_komputera >= 0:
    print("Możesz kupić komputer")
else:
    print(f"Brakuje ci jeszcze {cena_komputera - konto} zł")