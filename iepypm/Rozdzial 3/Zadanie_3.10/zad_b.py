def sprawdz_dlugosc(wiersz):
    for i in range(4):    
        if len(wiersz[i]) != len(wiersz[i + 1]):
               return False
    return True

def sprawdz_znak(znak, slowo):
    for i in range(len(slowo)):
        if slowo[i] == znak:
            return True;
    return False 

def sprawdz_anagram(wiersz):
    for j in range(1, 5):
        for i in range(len(wiersz[0])):    
            for k in range(len(wiersz[j])):
                if not sprawdz_znak(wiersz[j][k], wiersz[0]):
                    return False
    return True

def przepisz():
    dane = open("anagram.txt", "r")
    wyniki = open("odp_4b.txt", "w")
    for k in dane:
        wiersz = k.split()
        if sprawdz_dlugosc(wiersz):
            if sprawdz_anagram(wiersz):          
                wiersz = ' '.join(wiersz)
                wyniki.write(wiersz + '\n')
    dane.close()
    wyniki.close()

przepisz()
