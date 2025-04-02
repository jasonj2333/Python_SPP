def S(t):
    return 10000*(1.1)**t

def C(t):
    return 450 + 40*t

def D(t):
    return S(t)/C(t)

#lata = [0, 5, 10, 15, 20, 25]
lata = range(26)
srednia_na_sale = []

for rok in lata:
    print(rok, D(rok))
    srednia_na_sale.append(D(rok))
    
import matplotlib.pyplot as plt
plt.plot(lata, srednia_na_sale)
plt.show()