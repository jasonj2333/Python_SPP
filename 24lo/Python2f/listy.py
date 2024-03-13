uczniowie = ["Tomek", "Ilona", "Basia", "Anna", "Wojtek"]
print(uczniowie[0])
print(uczniowie[-1])
print( len(uczniowie) ) #długość listy

for imie in uczniowie:
    print(imie)
    
for index in range( len(uczniowie) ): #[0, 1, 2, 3, 4]
    print(index+1, uczniowie[index])