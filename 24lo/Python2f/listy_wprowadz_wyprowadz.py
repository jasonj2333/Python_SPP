N = 5
a = [0] * N

# print(a)
# a[2] = 5
# print(a)

def wprowadz_dane():
    for i in range(N):
        a[i] = int( input("Podaj liczbę: " ) )

def wyprowadz_dane():
    for i in range(N):
        print(f"a[{i}] = {a[i]}")

wprowadz_dane()
wyprowadz_dane()
    
    