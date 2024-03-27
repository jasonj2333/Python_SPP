import matplotlib.pyplot as plt

def D(m):
    return 264*m

def A(m):
    return 440 * m

def B(m):
    return A(m) - D(m)

def stopy_na_metry(stopy):
    return stopy * (30/100)

czas = [1,2,5,10,15,20]
metry = []

for minuta in czas:
    dystans_s = B(minuta)
    dystans_m = stopy_na_metry(dystans_s)
    metry.append(dystans_m)
    print(f"Wczasie {minuta} m Robert pokona {dystans_s} stóp tj. {dystans_m} metrów")

plt.plot(czas, metry)
plt.show()