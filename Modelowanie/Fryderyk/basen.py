def V(m):
    return 20 * m

def E(m):
    return 0.1 * m

def basen(start, m):
    return start + V(m) - E(m)

minuty = [0, 5, 10, 15, 20, 25, 30, 40]
start = 10000

for minuta in minuty:
    print(f"Woda w basen po {minuta} min wynosi {basen(start, minuta)}")