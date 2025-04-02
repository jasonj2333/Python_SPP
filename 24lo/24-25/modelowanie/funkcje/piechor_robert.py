def D(m):
    return 264*m

def A(m):
    return 440*m

def B(m):
    return A(m) - D(m)

def stopy_na_metry(stopy):
    return stopy / 3.2808

minuty = 15
wynik = B(minuty)
print( round(stopy_na_metry(wynik), 2) )

czas = [1,2,5,10,15,20]
metry = []

for minuty in czas:
    wynik = B(minuty)
    dystans_m = round(stopy_na_metry(wynik), 2)
    metry.append(dystans_m)
    print(f"W czasie {minuty} minut Robert pokona {dystans_m} m")

import matplotlib.pyplot as plt
plt.plot(czas, metry)
plt.show()