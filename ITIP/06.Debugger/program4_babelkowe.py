#sortowanie jest szybkie (liniowe) i stabilne (nie miesza elementów)
N = input('ile elementów? ')
#k = int(input('zakres od 0 do k, podaj k: '))

t = []
#k+=1
k = 20

for i in range(N):
    t.append(random.randrange(0, k))
    
print('tablica', t)

for j in range(N-1):
    for i in range(N-1-j): #za każdym obiegiem skraca się o j
        if t[i] > t[i+1]:
            c = t[i+1] #t[i], t[i+1] = t[i+1], t[i]
            t[i+1] = t[i]
            t[i] = c

print('tablica uporządkowana', t)