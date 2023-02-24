koszt_komputera = 5000
konto = 0

while konto < koszt_komputera:
    print("Stan konta: ", konto, ". Brakuje ci jeszcze: ", koszt_komputera - konto)
    wplata = int( input('Podaj wysokość wpłaty: ') )
    konto += wplata 

print("Koszt komputera: ", koszt_komputera)
print("Stan konta: ", konto)
print("Brawo, możesz kupić komputer")
if konto > koszt_komputera:
    print("Zostało ci jeszcze ", konto - koszt_komputera, " na gry!")