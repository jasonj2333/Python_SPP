#Zadanie Oskar
def A(d):
    return 10*d

def B(d):
    return 2 * d + d*d

def T(d):
    return A(d) + B(d)

kilometry = [10, 20, 50, 100, 500, 1000]

for d in kilometry:
    print(f"Oskar przeszedł {d} kilometrów i zarobił {T(d)} zł")
    