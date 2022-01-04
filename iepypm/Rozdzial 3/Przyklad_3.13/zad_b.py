def palindrom(s):
    return s == s[::-1]

def zad_b():
    minimum = ''
    maksimum = ''
    dl_minimum = 256
    dl_maksimum = 0
    suma = 0
    dane = open("slowa.txt", "r")
    wyniki1 = open("hasla_b.txt", "w")
    wyniki2 = open("slowa_b.txt", "w")
    wyniki2.write("1)\n")
    for s in dane:
        s = s.rstrip()
        wynik = ''
        pom = ''
        for i in range(len(s)):
            pom += s[i]    
            if palindrom(pom):
                w = pom
        if len(w) < len(s):
            wynik = s[len(s) - 1:len(w) - 1:-1]
        wynik += w
        if len(w) < len(s):
            wynik += s[len(w):len(s):]
        wyniki1.write(wynik + '\n') 
        if len(wynik) == 12: wyniki2.write(wynik + '\n') 
        if len(wynik) < dl_minimum: 
            minimum = wynik
            dl_minimum = len(wynik)                        
        if len(wynik) > dl_maksimum: 
            maksimum = wynik
            dl_maksimum = len(wynik)                        
        suma += len(wynik)
    dane.close();
    wyniki1.close();
    wyniki2.write("\n2)\n")
    wyniki2.write(minimum + '\n')
    wyniki2.write(maksimum + '\n')
    wyniki2.write("\n3)\n")
    wyniki2.write(str(suma))

zad_b()
