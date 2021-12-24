dane = open("dane1.18.txt", "r")
wyniki = open("wyniki1.18.txt", "w")
for k in dane:
    w = int(k) ** 2
    if w % 3 == 0:
        wyniki.write(str(w)+'\n')
dane.close()
wyniki.close()
