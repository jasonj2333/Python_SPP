# koniunkcja

def zad_a(a, b, c, d):
    if a < 5 and b < 5 and c < 5 and d < 5:
        print("TAK")
    else:
        print("NIE")

def zad_b(a, b, c, d):
    if a < 5:
        if b < 5:
            if c < 5:
                if d < 5: print("TAK")
                else: print("NIE")
            else: print("NIE")
        else: print("NIE")
    else: print("NIE")

zad_a(4, 6, 2, 3)
zad_b(4, 2, 1, 3)


