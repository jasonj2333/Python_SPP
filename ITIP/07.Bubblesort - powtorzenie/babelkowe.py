#lista elementów do posortowania
lista = [10, 34, 48, 26, 2, 44, 13, 24, 17, 37, 36, 29, 19, 37, 34, 32, 1, 31, 8, 38]
#lista = [1, 2, 8, 10, 13, 17, 19, 24, 26, 29, 31, 32, 34, 34, 36, 37, 37, 38, 44, 48]

#liczba elementów na liście - można to sprawdzić za pomocą funkcji len(lista)
N = 20 #len(lista)
j = 0
zamiany = 1
licznik = 0

#wyświetlanie elemnetów na liście
#print(lista)

for liczba in lista:
    print(f'{liczba}, ', end='')

print() #pusta linia

while j < N and zamiany != 0: #pętla warunkowa dopóki  j<liczba_elementów oraz zamiany!=0 wykonuj
    zamiany = 0
    
    for i in range(N-1-j): #pętla iteracyjna
        licznik += 1
        
        if lista[i] > lista[i+1]: #jeżeli elementy są nieodpowiedniej kolejności
            #zamiana elementów na liście
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
            #lista[i], lista[i+1] = lista[i+1], lista[i] # w Pythonie można prościej
            zamiany += 1
            
    j+=1

#wyświetlanie elementów listy
print(lista)

#wyświetlanie ilości porównań
print(licznik)

##### Algorytm w psedokodzie ze stronie - https://binarnie.pl/sortowaniebabelkowewcpp/
##### warto zajrzeć - https://visualgo.net/en/sorting

# dopóki  i<liczba_elementów oraz zamiany!=0 wykonuj
# 
#                 zamiany ←0
# 
#                 j ←0
# 
#                 dopóki j<liczba_elementów-1 wykonuj
# 
#                                jeśli  tab[j]>tab[j+1]
# 
#                                                zamień(tab[j],tab[j+1])
# 
#                                                zamiany←zamiany+1
# 
#                                j ← j+1
# 
#                 i ← i+1