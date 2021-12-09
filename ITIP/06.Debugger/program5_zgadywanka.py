from random import randint
a = 1
b = 100
x = randint(a,b)
y = 0

while x!=y:
    y = int(input("Podaj liczbe: "))
    #y = (a+b)//2 #symulacja komputer gra sam
    print(y, end=' ')
    if y < x:
        print("Za duzo")
        #a = y #do wersji symulacyjnej
    elif y > x:
        print("Za malo")
        #b = y #do wersji symulacyjnej

#end while
print("Dobrze")
        


