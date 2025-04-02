from math import sin, cos, pi
from random import randint

liczba_rund = 100
brown_X = [0]
brown_Y = [0]
r = 1

for runda in range(1, liczba_rund + 1):
    fi = float(randint(0, 360)) * pi / 180
    stare_X = brown_X[runda-1]
    stare_Y = brown_Y[runda-1]
    nowe_X = stare_X + (r * cos(fi))
    nowe_Y = stare_Y + (r * sin(fi))
    brown_X.append(nowe_X)
    brown_Y.append(nowe_Y)

#print(f"Wartość X = {brown_X}")
#print(f"Wartość Y = {brown_Y}")

import matplotlib.pyplot as plt
import numpy as np

plt.plot(brown_X, brown_Y, "o:", color="green")
plt.show()


