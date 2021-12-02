#samogloski
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

tekst = input('Podaj tekst: ')

licznik = 0;

zlicz = {}

for znak in tekst.lower():
    if znak in samogloski:
        licznik += 1
        if znak not in zlicz:
            zlicz[znak] = 0
        zlicz[znak] +=1
        
print(f'W podanym tekście jest {licznik} samogłosek')
print(zlicz)




        
    