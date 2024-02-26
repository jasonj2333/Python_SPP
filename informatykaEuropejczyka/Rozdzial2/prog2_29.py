#wyznaczanie miejsca zerowego funkcji w przedziale [p, q]

def F (x):
    return x**2-x-3

def oblicz (p, q, E1):
    s=(p+q)/2
    while F(p)!=0 and F(q)!=0 and q-p>=E1:
        s=(p+q)/2;
        if F(p)*F(s)>0:
            p=s
        else:
            q=s
    if F(p)==0:
        return p
    if F(q)==0:
        return q
    return s

#print(oblicz(-2,5,0.001))

