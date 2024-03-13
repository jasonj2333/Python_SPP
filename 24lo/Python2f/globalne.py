def obwod():
    return 4 * bok

def pole(a):
    return a * a

# def zmien_bok():
#     global bok
#     bok = 9

def zmien_bok(a):
    a = 9
    return a

bok = int( input("Podaj bok kwadratu: ") )
bok = zmien_bok(bok)
wynik = obwod()
wynik2 = pole(bok)
print(f"Obwód kwadratu wynosi: {wynik}")
print(f"Pole kwadratu wynosi: {wynik2}")