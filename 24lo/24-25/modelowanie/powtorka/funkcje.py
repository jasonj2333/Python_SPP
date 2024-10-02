import math

def prostokat(a, b):
    return a * b

def kwadrat(a):
    return prostokat(a, a)

def trojkat(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def kolo(r):
    return math.pi * r * r

def menu():
    print("Wybierz figurę:")
    print("1. Prostokąt")
    print("2. Kwadrat")
    print("3. Trójkąt")
    print("4. Koło")
    
def pola_figur():
    menu()
    wybor = int( input("Wybierz 1-4:") )
    if(wybor < 1 or wybor > 4):
        print("Błędny wybór")
        return
    
    if(wybor == 1):
        a = int( input("Podaj długość boku a: ") )
        b = int( input("Podaj długość boku b: ") )
        pole = prostokat(a, b)
        print(f"Pole prostokąta o bokach {a} i {b} = {pole}")
    elif(wybor == 2):
        a = int( input("Podaj długość boku a: ") )
        pole = kwadrat(a)
        print(f"Pole kwadratu o boku {a} = {pole}")
    elif(wybor == 3):
        a = int( input("Podaj długość boku a: ") )
        b = int( input("Podaj długość boku b: ") )
        c = int( input("Podaj długość boku c: ") )
        pole = trojkat(a, b, c)
        print(f"Pole trójkąta o boku {a}, {b}, {c} = {pole}")
    elif(wybor == 4):
        r = int( input("Podaj promień r: ") )
        pole = kolo(r)
        print(f"Pole koła o promieniu {r} = {pole}") 

pola_figur()
    
    