# algorytm wyznaczający pierwiastki równania liniowego ax+b=0

def rownanie_liniowe(a, b):
    if a != 0:
        x = -b / a
        print("x = ", x)
    elif b == 0:
        print("nieskończenie wiele rozwiązań")
    else: print("równanie sprzeczne")

rownanie_liniowe(-2, 5)


