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

source_number = input('Podaj liczbę do konwersji: ')
from_system = int(input('Podaj podstawę systemu źródłowego: ')) 
to_system = int(input('Podaj podstawę systemu docelowego: '))

results = dec_to_sys(sys_to_dec(source_number, from_system), to_system)

print(results)