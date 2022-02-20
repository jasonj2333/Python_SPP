def dostawy(l_dostaw):
    suma = 0

    for i in range(l_dostaw): #[0, 1, 2, 3, 4]
        ile = int(input(f"Podaj liczbę egzemplarzy w {i+1} dostawie: "))
        suma += ile #suma = suma + ile

    return suma

print("Dostawy telewizorów: ")
l_dostaw_tv = int(input("Podaj liczbę dostaw telewizorów: "))
suma_tv = dostawy(l_dostaw_tv)
print(f"Liczba telewizorów z {l_dostaw_tv} dostaw wynosi {suma_tv}")

print("\nDostawy głośników: ")
l_dostaw_glosnikow = int(input("Podaj liczbę dostaw głośników: "))
suma_glosnikow = dostawy(l_dostaw_glosnikow)
print(f"Liczba głośników z {l_dostaw_glosnikow} dostaw wynosi {suma_glosnikow}")