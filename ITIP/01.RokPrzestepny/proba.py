rok = int(input("Podaj rok: "))

przez4 = rok % 4
przez100 = rok % 100
przez400 = rok % 400

if (przez4 == 0 and przez100 != 0) or przez400 == 0:
    print(f"{rok} jest przestępny")
else:
    print(f"{rok} nie jest przestępny")
    
a = 2    
if a > 4:
    a = 10
elif a < 4 and a > 1:
    a = 0
else:
    a = 123