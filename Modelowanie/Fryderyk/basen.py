import matplotlib.pyplot as plt

def V(m):
    return 20 * m

def E(m):
    return 0.1 * m

def basen(start, m):
    return start + V(m) - E(m)

minuty = [0, 5, 10, 15, 20, 25, 30, 40]
start = 10000
napelnienie = []

for minuta in minuty:
    print(f"Woda w basen po {minuta} min wynosi {basen(start, minuta)}")
    napelnienie.append(basen(start, minuta))

plt.plot(minuty, napelnienie)
plt.show()