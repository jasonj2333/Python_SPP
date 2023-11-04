import math

czas = [[0 for j in range(3)] for i in range(1095)]
temp = [[0 for j in range(3)] for i in range(1095)]

files = [ open("dane_systemy1.txt", "r"), open("dane_systemy2.txt", "r"), open("dane_systemy3.txt", "r") ]

for p in range(3):
    system = pow(2, p+1)
    lines = files[p].readlines()
    i = 0
    for line in lines: 
        words = line.split()
        czas[i][p], temp[i][p] = int(words[0], system), int(words[1], system)
        i += 1

########## 58.1 ##########

def najmniejsza_temp(temp):
    minimalne = [temp[0][0], temp[0][1], temp[0][2]]  
    for j in range(3):
        for i in range(1, 1095):
            if minimalne[j] > temp[i][j]:
                minimalne[j] = temp[i][j]
        minimalne[j] = bin(minimalne[j])
        if minimalne[j][0] == "-":
            minimalne[j] = "-" + minimalne[j][3:]
        else:
            minimalne[j] = minimalne[j][2:]
    return minimalne

print("Temperatury min = ", najmniejsza_temp(temp))

########## 58.2 ##########

def znajdz_zepsute(czas):
    ile_zepsutych = 0
    licznik = 12
    for i in range(1, 1095):
        licznik += 24
        if czas[i][0] != licznik and czas[i][1] != licznik and czas[i][2] != licznik:
            ile_zepsutych += 1     
    return ile_zepsutych

print("Zepsutych pomiarów jednocześnie = ", znajdz_zepsute(czas))

########## 58.3 ##########

def znajdz_rekordowe_dni(temp):
    dotychczasowy_rekord = [temp[0][0], temp[0][1], temp[0][2]]
    ile_dni_rekordowych = 1
    for i in range(1, 1095):
        jest_dzien_rekordowy = False
        for j in range(3):
            if temp[i][j] > dotychczasowy_rekord[j]:
                dotychczasowy_rekord[j] = temp[i][j]
                if not jest_dzien_rekordowy:
                    ile_dni_rekordowych +=1
                    jest_dzien_rekordowy = True
    return ile_dni_rekordowych

print("Rekordowych dni = ", znajdz_rekordowe_dni(temp))

########## 58.4 ##########

def wyznacz_max_skok(temp):
    maks_skok = 0
    for i in range(1094):
        for j in range(i+1, 1095):
            r = pow((temp[i][0] - temp[j][0]), 2)
            skok = math.ceil(r / abs(i-j))
            if skok > maks_skok:
                maks_skok = skok
    return maks_skok

print("Rekordowy skok = ", wyznacz_max_skok(temp))

for f in files:
    f.close()