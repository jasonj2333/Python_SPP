def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print( nwd(81, 54) )
print( nwd(1563, 66) )
print( nwd(13, 95) )

def nwd2(a, b):
    while b > 0:
        pom = a
        a = b
        b = pom % b
    return a
    
print( nwd2(81, 54) )
print( nwd2(1563, 66) )
print( nwd2(13, 95) )

#rozwiazanie rekurencyjne - nieobowiązkowe
def nwd3(a, b):
    if b > 0:
        return nwd3(b, a % b)
    return a

import math
print(math.gcd(81, 54))

def nww(a, b):
    return a*b // nwd2(a, b)

print(nww(6, 9))

