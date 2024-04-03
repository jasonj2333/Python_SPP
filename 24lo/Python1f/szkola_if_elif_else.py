# Zapytaj użytkownika o rok urodzenia
# Oblicz ile ma lat i zapisz to w zmiennej wiek
# 
# Jeżeli wiek < 3 to wypisz "Jesteś jeszcze mały"
# Jeżeli wiek < 7 to wypisz "Pewnie chodzisz do przedszkola"
# Jeżeli wiek <= 14 to wypisz "Pewnie chodzisz do SP"
# Jeżeli wiek <= 19 to wypisz "Pewnie chodzi do SPP"
# Jeżeli wiek <= 24 to wypisz "Pewnie jesteś na studiach"
# W przeciwnym razie wypisz "Pewnie już pracujesz"

rok_urodzenia = int( input("Podaj rok urodzenia: " ) )
wiek = 2024 - rok_urodzenia

if wiek < 3:
    print("Jesteś jeszcze mały")
elif wiek < 7:
    print("Pewnie chodzisz do przedszkola")
elif wiek <= 14:
    print("Pewnie chodzisz do SP")
elif wiek <= 19:
    print("Pewnie chodzi do SPP")
elif wiek <= 24:
    print("Pewnie jesteś na studiach")
else:
    print("Pewnie już pracujesz")
