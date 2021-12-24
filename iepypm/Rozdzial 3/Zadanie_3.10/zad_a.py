def sprawdz_dlugosc(wiersz):
    for i in range(4):    
        if len(wiersz[i]) != len(wiersz[i + 1]):
               return False
    return True

def przepisz():
    dane = open("anagram.txt", "r")
    wyniki = open("odp_4a.txt", "w")
    for k in dane:
        wiersz = k.split()
        if sprawdz_dlugosc(wiersz):
            wiersz = ' '.join(wiersz)
            wyniki.write(wiersz + '\n')
    dane.close()
    wyniki.close()

przepisz()
