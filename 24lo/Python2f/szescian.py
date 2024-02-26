bok = 1

while bok > 0:
    bok = int( input("Podaj bok sześcianu: ") )
    if(bok > 0):
        objetosc = bok ** 3
        print(f"Objętość sześcianu wynosi: {objetosc}")
    else:
        print("To nie jest poprawny bok sześcianu")