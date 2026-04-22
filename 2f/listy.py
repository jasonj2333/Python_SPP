klasa2f = ["Wiktor", "Andrii", "Mateusz", "Arkadiusz", "Julia", "Alicja"]
print(klasa2f[4])
n = len(klasa2f)
print(n)
print(klasa2f[n-1])

klasa2f.append("Mikołaj") #dodaje na końcu listy
print(klasa2f[-1])
print()

for uczen in klasa2f:
    print(uczen)
    
print()

for index, uczen in enumerate(klasa2f):
    print(index+1, uczen)
    
print()

for i in range(len(klasa2f)):
    print(i, klasa2f[i])
    
print("Lista uporządkowana:")
for uczen in sorted(klasa2f):
    print(uczen)
    
print(klasa2f)
klasa2f.sort()
print(klasa2f)