import matplotlib.pyplot as plt
import numpy as np

def R(n):
    return 18*n

def P(n):
    return 17*n - 5

def E(n):
    return R(n) - P(n)

parasole = [200, 500, 1000, 5000, 10000]
koszty = []

for p in parasole:
    print(f"Sprzedane parasole: {p} | koszt: {E(p)} | dochód: {P(p)}")
    koszty.append( E(p) )

x = np.linspace(0, 10000, 100)
plt.plot(x, E(x))
plt.show()