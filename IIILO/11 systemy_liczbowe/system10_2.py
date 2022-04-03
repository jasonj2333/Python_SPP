dziesietna = 123

def dec_to_bin(liczba):
    res = ''
    while liczba > 0:
        reszta = liczba % 2
        res = str(reszta) + res
        liczba = liczba // 2
    return res

def dec_to_sys(liczba, podstawa):
    res = ''
    while liczba > 0:
        reszta = liczba % podstawa
        if reszta > 9:
            res = chr(55 + reszta) + res
        else:
            res = str(reszta) + res
        liczba = liczba // podstawa
    return res

print(dec_to_bin(dziesietna))
print(bin(dziesietna))

print(dec_to_sys(dziesietna, 16))
print(hex(dziesietna))
    
