#samogloski ze zliczaniem
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

tekst = input('Podaj tekst: ')

licznik = 0;

for znak in tekst.lower():
    if znak in samogloski:
        licznik += 1
        
print(f'W podanym tekście jest {licznik} samogłosek')





        
    