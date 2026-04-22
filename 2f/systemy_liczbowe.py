liczba = int(input("Podaj liczbę: "))

def dec_to_bin(liczba):
    result = ""
    while liczba > 0:
        reszta = liczba % 2
        result = str(reszta) + result
        liczba = liczba // 2
    return result

print(dec_to_bin(liczba))

liczba_bin = "1100111"

def bin_to_dec(liczba):
    potega = 1
    dziesietna = 0
    
    for i in range(len(liczba)-1, -1, -1):
        dziesietna += int(liczba[i]) * potega
        potega *= 2
    return dziesietna

print( bin_to_dec(liczba_bin) )