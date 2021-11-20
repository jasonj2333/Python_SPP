from math import sqrt
n = 19

for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        print('NIE')
        break
else: print('TAK')