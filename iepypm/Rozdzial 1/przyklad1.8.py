# znajdowanie elementu minimalnego

def minimum(n):
    k = float(input("podaj liczbę: "))
    min = k
    while n > 1:
        k = float(input("podaj liczbę: "))
        if k < min:
            min = k
        n -= 1
    return min    

print(minimum(5))
