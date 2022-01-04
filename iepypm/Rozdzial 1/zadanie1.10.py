def zad():
    x=0
    y=1
    z=2
    for i in range(5):
        for j in range(5):
            if i % 2 == 0:
                if j == 1 or j == 3: print(x)
                else: print(z)
            else:
                if (j + 1) % 3 != 0: print(y)
                else: print(x)

zad()


