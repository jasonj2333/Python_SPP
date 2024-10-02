from datetime import datetime

rok_szkolny = input("Podaj rok szkolny: ")
print("Witamy w nowym roku szkolnym", rok_szkolny, "!!!")
print(f"Witamy w nowym roku szkolnym {rok_szkolny} !!!")

wiek = int( input("Podaj rok urodzenia: ") )
#print(f"Masz {2024 - wiek} lat")

def oblicz_wiek(rok_urodzenia):
    data_biezaca = datetime.now()
    return data_biezaca.year - rok_urodzenia

print(f"Masz {oblicz_wiek(wiek)} lat")

if oblicz_wiek(wiek) >= 18:
    print("Możesz głosować w wyborach")
elif oblicz_wiek(wiek) == 17:
    print("Za rok będziesz mógł zagłosować")
else:
    print("Nie masz jeszcze praw wyborczych")
    
def menu():
    print("Menu programu:")
    print("1. Przegląd możliwości")
    print("2. Import danych")
    print("3. Eksport danych")
    
menu()