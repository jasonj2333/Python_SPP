# alternatywa

def zad_a(x, y, z):
    if x % 2 or y % 2 or z % 2:
        print("TAK")
    else:
        print("NIE")

def zad_b(x, y, z):
    if x % 2:
        print("TAK")
    elif y % 2:
        print("TAK")
    elif z % 2:
        print("TAK")
    else:
        print("NIE")
    
zad_a(4, 6, 2)
zad_b(4, 5, 2)

