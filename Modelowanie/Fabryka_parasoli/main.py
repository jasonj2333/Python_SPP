import matplotlib.pyplot as plt
import numpy as np

#przychod
def R(n):
    return 18 * n

#zysk
def P(n):
    return 17 * n - 5

#koszty
def E(n):
    return R(n) - P(n)

parasole = [200, 500, 1000, 5000, 10000]
for p in parasole:
    print(f"Sprzedane parasole: {p}.\nKoszt prowadzenia firmy: {E(p)}")

x = np.linspace(200, 10000, 100)

plt.plot(x, E(x))
plt.show()