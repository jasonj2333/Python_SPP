from math import sqrt,sin,cos,pi
from random import randint

liczba_rund = 100
r = 1
liczba_cz = 3
czastki = []

def brown():
    brown_X = [0]
    brown_Y = [0]
    for runda in range(1,liczba_rund + 1):
        # wylosowany kąt musi być podany w radianach; wymagają tego funkcje sin() i cos()
        fi = float(randint(0, 360)) * pi / 180
        stare_x = brown_X[runda-1]
        nowe_x = stare_x + (r * cos(fi))
        stare_y = brown_Y[runda-1]
        nowe_y = stare_y + (r * sin(fi))
        brown_X.append(nowe_x)
        brown_Y.append(nowe_y)
        
#     print(f"Wartości X = {brown_X}")
#     print(f"Wartości Y = {brown_Y}")
    czastki.append([brown_X, brown_Y])
    
for i in range(liczba_cz):
    brown()

# wczytujemy moduł i ustawiamy alias, który będziemy używać w kodzie
import matplotlib.pyplot as plt
import numpy as np

#linie układu współrzednych
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

plt.axis((-20, 20, -20, 20))
# plt.xticks(np.arange(-20, 20+1, 2))
# plt.yticks(np.arange(-20, 20+1, 2))

# wywołujemy metodę plot z parametrami:
# brown_X - tablica współrzędnych x
# brown_Y - tablica współrzędnych y
# "o:" - określenie rodzaju punktów i linii
# color="green" - określenie koloru
# linewidth=2 - określenie szerokości linii
for i in range(liczba_cz):
    plt.plot(czastki[i][0], czastki[i][1], "o:", linewidth=2)


# dodajemy opis współrzędnych oraz tytuł
plt.xlabel("Współrzędne X")
plt.ylabel("Współrzędne Y")
plt.title("Ruchy Browna")

# włączamy widoczność pomocniczej siatki współrzędnych
plt.grid(True)

# uruchamiamy okno wykresu
plt.show()