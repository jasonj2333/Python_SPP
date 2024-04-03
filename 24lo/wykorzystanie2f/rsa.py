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

def decryption(c, prk):
    d = prk[0]
    n = prk[1]
    
    return c ** d % n

p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)
e = public_key(phi)
d = private_key(phi, e)

pub_key = (e, n)
print(pub_key)
priv_key = (d, n)
print(priv_key)

#szyfrowanie
cipher = encryption( ord('J'), pub_key)
print(chr(cipher))

#deszyfrowanie
plain_text = decryption(cipher, priv_key)
print(chr(plain_text))

message = "pierwszydzienwiosny"
cipher = []

for c in message:
    cipher.append( encryption( ord(c), pub_key) )
print(cipher)

plain_text = ""
for c in cipher:
    plain_text += chr( decryption(c, priv_key) )
print(plain_text)


