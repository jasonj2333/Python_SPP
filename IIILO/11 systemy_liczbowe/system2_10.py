binarna = '1101'

def bin_to_dec(binarna):
    potega = 1
    dziesietna = 0
    
    for i in range(len(binarna)-1, -1, -1):
        dziesietna += int(binarna[i])*potega
        potega *= 2
    return dziesietna

def sys_to_dec(liczba, podstawa):
    potega = 1
    dziesietna = 0
    
    for i in range(len(liczba)-1, -1, -1):
        if liczba[i].isdigit():
            dziesietna += int(liczba[i])*potega
        else:
            dziesietna += (ord(liczba[i].upper())-55)*potega
        potega *= podstawa
    return dziesietna

print(bin_to_dec(binarna))
print(int(binarna, 2))

print(sys_to_dec('7b', 16))
