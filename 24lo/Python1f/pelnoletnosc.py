wiek = int( input("Ile masz lat: " ) )

if wiek >= 18:
    print("Jesteś dorosły")
else:
    print("Nie jesteś jeszcze dorosły")
    print(f"Do pełnoletności brakuje ci jeszcze {18 - wiek} lata")