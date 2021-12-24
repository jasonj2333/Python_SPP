wyniki1 = open("dane1.22.txt", "w")
lista = ["styczeń\n", "luty\n", "marzec\n", "kwiecień\n", "maj\n", "czerwiec\n", "lipiec\n", "sierpień\n", "wrzesień\n", "październik\n", "listopad\n", "grudzień\n"]
wyniki1.writelines(lista)
wyniki1.close()

wyniki1 = open("dane1.22.txt", "r")
for k in wyniki1:
    if k[0] == 'm':
        print(k)
wyniki1.close()

wyniki1 = open("dane1.22.txt", "r")
wyniki2 = open("wyniki1.22.txt", "w")
for k in wyniki1:
    if len(k.rstrip()) > 8:
        wyniki2.write(k)
wyniki1.close()
wyniki2.close()

wyniki2 = open("wyniki1.22.txt", "r")
print(wyniki2.read())
wyniki2.close()


