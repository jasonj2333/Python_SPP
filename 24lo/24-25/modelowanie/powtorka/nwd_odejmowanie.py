# K01: Dopóki a ≠ b:
#      wykonuj krok K02
# K02:   Jeśli a < b, 
#        to      b ← b-a ; od większej liczby odejmujemy
#        inaczej a ← a-b ; mniejszą aż się zrównają
# K03: Pisz a            ; wtedy dowolna z nich jest NWD
# K04: Zakończ

def nwd1(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a

print( nwd1(19,10) )
print( nwd1(27,4) )

# K01: Dopóki b ≠ 0:
#      wykonuj kroki K02…K04
# K02:   t ← b ; zapamiętujemy dzielnik
# K03:   b ← a mod b ; reszta z dzielenia staje się dzielnikiem
# K04:   a ← t ; poprzedni dzielnik staje się dzielną
# K05: Pisz a ; NWD jest ostatnią dzielną
# K06: Zakończ

def nwd2(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print( nwd2(279, 37) )
print( nwd2(81, 45) )

def nww(a, b):
    return a*b // nwd2(a,b)

print( nww(4, 6) )

    