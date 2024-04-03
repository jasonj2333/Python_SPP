#Wypisz na ekranie co drugą od 5 do 25
for i in range(5, 26, 2):
    print(i)
    
#Wypisz na ekranie 10 kolejnych liczb całkowitych
#począwszy od 12
for i in range(12, 22):
    print(i)
    
#Wypisz na ekranie 10 liczb zaczynając od 6 z których
#każda kolejna jest większa od poprzedniej o 17
n = 50
start = -9
skok = 6
stop = n * skok
for i in range(start, stop, skok):
    print(i)
    
for i in range(100, 5, -5):
    print(i)