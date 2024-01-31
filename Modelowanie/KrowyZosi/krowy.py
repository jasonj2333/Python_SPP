#krowy
def C(t):
    return 30 * 2**t

#siano na krowę
def F(t):
    return 8 * 1.5**t

#siano do karmienia
def H(t):
    return C(t) * F(t)

t = 5
print(H(t))
#print(240 * 3**t)

