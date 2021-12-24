def zad_a():
    minimum = ''
    maksimum = ''
    dl_minimum = 256
    dl_maksimum = 0
    dane = open("slowa.txt", "r")
    wyniki1 = open("hasla_a.txt", "w")
    wyniki2 = open("slowa_a.txt", "w")
    for s in dane:
        w = s[::-1].strip()
        wyniki1.write(w + '\n')
        if len(w) < dl_minimum: 
            minimum = w
            dl_minimum = len(w)                        
        if len(w) > dl_maksimum: 
            maksimum = w
            dl_maksimum = len(w)    
    wyniki2.write(str(minimum) + "\t" + str(dl_minimum) + '\n')
    wyniki2.write(str(maksimum) + "\t" + str(dl_maksimum) + '\n')
    dane.close();
    wyniki1.close();
    wyniki2.close();

zad_a()
