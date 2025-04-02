liczba = 124

def dec_to_bin(liczba):
    res = ""
    while liczba != 0:
        reszta = liczba % 2
        res = str(reszta) + res
        liczba = liczba // 2
    return res

print( dec_to_bin(liczba) )
print( dec_to_bin(2025) )

def bin_to_dec(binarna):
    dziesietna = 0
    waga = 1
    
    for i in range(len(binarna)-1, -1, -1):
        dziesietna += int(binarna[i]) * waga
        waga *= 2
    return  dziesietna

print( bin_to_dec('11001100') )
print( bin_to_dec('11111111') )

        
    
    
    