#jedynki 1 + 11 + 111 + 1111 + .... + 1......1

n = 6
suma = 0
next = 0

for i in range(1, n+1):
    next = next * 10 + 1
    #print(next)
    suma += next
    
print(suma)
    