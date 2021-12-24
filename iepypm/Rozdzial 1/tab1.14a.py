# pobieranie zawartości pliku wiersz po wierszu w pętli
odczyt = open("dane1.14.txt", "r")
for k in odczyt:
    print(k.rstrip())
odczyt.close()

print()

# odczytywanie całego pliku
odczyt = open("dane1.14.txt", "r")
print(odczyt.read())
odczyt.close()

print()

# odczytywanie znaków z pliku
odczyt = open("dane1.14.txt", "r")
print(odczyt.read(2))
print(odczyt.read(5))
odczyt.close()

print()

# odczytywanie znaków z wiersza
odczyt = open("dane1.14.txt", "r")
print(odczyt.readline(3))
print(odczyt.readline(2))
odczyt.close()

print()

# odczytywanie po jednym wierszu
odczyt = open("dane1.14.txt", "r")
print(odczyt.readline())
print(odczyt.readline())
print(odczyt.readline())
print(odczyt.readline())
odczyt.close()

print()

# wczytywanie całego pliku do listy
odczyt = open("dane1.14.txt", "r")
lista = odczyt.readlines()
print(lista)
print(len(lista))
for k in lista:
    print(k.rstrip())
odczyt.close()






