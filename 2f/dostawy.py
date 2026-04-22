def dostawy(n):
    suma = 0
    for i in range(n):
        towar = int( input("Podaj liczbę sztuk: ") )
        suma += towar
    return suma

print("Telewizory:")
ldostaw = 3
sumaTV = dostawy(ldostaw)
print(f"Suma dostaw TV wynosi: {sumaTV}")

print("Pralki")
ldostaw = 4
sumaPralki = dostawy(ldostaw)
print(f"Suma dostaw pralek wynosi: {sumaPralki}")