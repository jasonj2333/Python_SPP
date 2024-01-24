ladownosc = 3500
paczki = [1620, 18, 1]
zaladowano = [0, 0, 0]

for i in range(len(paczki)):
    zaladowano[i] = ladownosc // paczki[i]
    ladownosc -= zaladowano[i] * paczki[i]
    
print(zaladowano)
print(ladownosc)