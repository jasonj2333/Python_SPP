pkt = int( input("Podaj dotychczasową liczbę punktów: ") )
f = float( input("Podaj frekwencję w ostatnim półroczu: ") )
so = float( input("Podaj średnią ocen w ostatnim półroczu: ") )

if f > 94 and so >= 4.0:
    pkt += 20

print(f"Liczba punktów klasy wynosi: {pkt}")