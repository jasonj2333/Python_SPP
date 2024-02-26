a = 8
b = 4

def nwd_rek(a, b):
    if b!=0:
        return nwd_rek(b, a % b)
    return a

print( nwd_rek(81, 18) )