dane = open("dane1.23.txt", "r")
wyniki = open("wyniki1.23.txt", "w")
for k in dane:
    m = k.split()
    z = int(m[0]) * int(m[1])
    if z >= 250 and z <= 3000:
        wyniki.write(str(z) + '\n')
dane.close()
wyniki.close()
