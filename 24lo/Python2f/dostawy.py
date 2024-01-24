def suma_dostaw(n, typ=""):
    suma = 0
    for i in range(n):
        dostawa = int( input(f"Jaka jest liczba sztuk {typ} w {i+1} dostawie: ") )
        if dostawa > 0:
            suma += dostawa
        else:
            print("Błędna wartość")
    return suma

l_dostaw_tv = 3
suma_dostaw_tv = suma_dostaw(l_dostaw_tv, "telewizorów")
print(f"Suma dostaw telewizorów wynosi: {suma_dostaw_tv}")

l_dostaw_glosnikow = 4
suma_dostaw_glosnikow = suma_dostaw(l_dostaw_glosnikow, "głośników")
print(f"Suma dostaw głośników wynosi: {suma_dostaw_glosnikow}")