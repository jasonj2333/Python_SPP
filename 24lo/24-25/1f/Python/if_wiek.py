wiek = int( input("Podaj swój rok urodzenia: ") )

if 2024-wiek >= 18:
    print("Możesz kupić napój energentyczny")
else:
    brakuje = 18 - (2024-wiek)
    print(f"Przyjdź za {brakuje} lat")