from math import sqrt

a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

if a + b > c and b + c > a and a + c > b:
    p = (a + b + c) / 2 #polowa obwodu trojkata
    P = sqrt(p*(p-a)*(p-b)*(p-c)) #wzór Herona
    print(f"Pole trójkąta wynosi: {P}")
else:
    print("Podane boki nie tworzą trójkąta")
