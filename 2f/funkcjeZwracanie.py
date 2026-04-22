def suma(a, b):
    wynik = a + b
    return wynik

def roznica(a, b):
    return a - b

#iloczyn *
def iloczyn(a, b):
    return a* b
#iloraz /
def iloraz(a, b):
    if(b == 0):
        return "Nie wolno dzielić przez 0"
    return a / b

print( suma(5, 6) )
wynik = suma(11, 7)
print(wynik)
print(roznica(49, 34))
print(iloczyn(6, 8))
print(iloraz(49, 0))