rok_urodzenia = int(input("Podaj rok urodzenia: "))
wiek = 2026 - rok_urodzenia

if wiek >= 18:
    print("Możesz kupić napój energetyczny")
else:
    print("Niestety, nie możesz kupić napoju energetycznego")