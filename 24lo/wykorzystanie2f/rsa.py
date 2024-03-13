def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def public_key(phi):
    i = 2
    n_w_d = nwd(phi, i)
    while n_w_d != 1:
        i += 1
        n_w_d = nwd(phi, i)
    return i

def private_key(phi, e):
    i = 1
    while (phi * i + 1) % e != 0:
        i += 1
    return int( (phi * i + 1) / e )

def encryption(t, pbk):
    e = pbk[0]
    n = pbk[1]
    
    return t**e % n

p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)
e = public_key(phi)
d = private_key(phi, e)

pub_key = (e, n)
print(pub_key)