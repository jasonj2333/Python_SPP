dane = open("dane1.17.txt", "r")
wyniki = open("wyniki1.17.txt", "w")
for k in dane:
    if len(k.rstrip()) % 2 == 0:
        wyniki.write(k)
dane.close()
wyniki.close()

