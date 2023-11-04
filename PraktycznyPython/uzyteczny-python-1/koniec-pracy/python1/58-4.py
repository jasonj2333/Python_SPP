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
		
########## 58.4 ##########

# Metoda poszukiwania ekstremum (akurat tutaj maksimum)
# jest taka sama, jakiej użyliśmy w punkcie 58.1

def wyznacz_max_skok(temp):
    # Python posiada moduł math - funkcje w nim zawarte warto znać (szczególnie na maturze)
    # Więcej informacji o module - zajrzyj: https://docs.python.org/3/library/math.html
    # Deklarujemy import modułu math
    import math
    
    # Zmienna poniżej przechowa skok o największej wartości
    najwiekszy = 0
    
    # Podwójna pętla wyznaczająca skoki temperatur
    for i in range(1094):
        for j in range(i+1, 1095):

            # ceil() to zaokrąglanie w górę (ang. ceiling = sufit)
            # pow() to potęgowanie (ang. power = potęga)
            # abs() to wartość bezwzględna (ang. absolute value)
            
            skok = math.ceil(pow(temp[i][0] - temp[j][0], 2) / abs(i-j))
            
            # jeżeli mamy największy do tej pory napotkany skok, wkładamy go do zmiennej przechowującej maksimum
            if (najwiekszy < skok):
                najwiekszy = skok
                
    return najwiekszy

print("Rekordowy skok = ", wyznacz_max_skok(temp))