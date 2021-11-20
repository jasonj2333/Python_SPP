from math import sqrt
n = 2

def pierwsza1(n):
    pom = int(sqrt(n))+1
    for i in range(2, pom):
        if n % i == 0:
            return False
    return True

def pierwsza2(n):
    pom = int(sqrt(n))+1
    i = 2
    while i <= pom:
        if n % i == 0:
            return False
        i+=1
    return True

def pierwsza3(n):
    pom = int(sqrt(n))+1
    if n % 2 == 0:
        return n == 2
    for i in range(3, pom, 2):
        if n % i == 0:
            return False
    return True

print(pierwsza1(n))
print(pierwsza3(n))
        
