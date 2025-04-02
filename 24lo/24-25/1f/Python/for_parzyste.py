#Wypisz wszystkie liczby parzyste z przedziału od <0 do 100>

for i in range(101):
    if i % 2 == 0:
        print(i)
        
for i in range(0, 101, 2):
    print(i)
    