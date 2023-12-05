from math import sqrt,sin,cos,pi
from random import randint

liczba_rund = 100
r = 1
cz1_X = [0]
cz1_Y = [0]

cz2_X = [0]
cz2_Y = [0]

def brown(brown_X, brown_Y):
    for runda in range(1,liczba_rund + 1):
        # wylosowany kąt musi być podany w radianach; wymagają tego funkcje sin() i cos()
        fi = float(randint(0, 360)) * pi / 180
        stare_x = brown_X[runda-1]
        nowe_x = stare_x + (r * cos(fi))
        stare_y = brown_Y[runda-1]
        nowe_y = stare_y + (r * sin(fi))
        brown_X.append(nowe_x)
        brown_Y.append(nowe_y)
        
    print(f"Wartości X = {brown_X}")
    print(f"Wartości Y = {brown_Y}")
    
brown(cz1_X, cz1_Y)
brown(cz2_X, cz2_Y)

# wczytujemy moduł i ustawiamy alias, który będziemy używać w kodzie
import matplotlib.pyplot as plt
import numpy as np

#linie układu współrzednych
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

plt.axis((-10, 10, -10, 10))
# plt.xticks(np.arange(-20, 20+1, 2))
# plt.yticks(np.arange(-20, 20+1, 2))

# wywołujemy metodę plot z parametrami:
# brown_X - tablica współrzędnych x
# brown_Y - tablica współrzędnych y
# "o:" - określenie rodzaju punktów i linii
# color="green" - określenie koloru
# linewidth=2 - określenie szerokości linii
plt.plot(cz1_X, cz1_Y, "o:", linewidth=2)
plt.plot(cz2_X, cz2_Y, "o:", linewidth=2)

# dodajemy opis współrzędnych oraz tytuł
plt.xlabel("Współrzędne X")
plt.ylabel("Współrzędne Y")
plt.title("Ruchy Browna")

# włączamy widoczność pomocniczej siatki współrzędnych
plt.grid(True)

# uruchamiamy okno wykresu
plt.show()