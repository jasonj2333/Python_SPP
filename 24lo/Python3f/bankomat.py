nominaly = [100, 50, 20, 10, 5, 2, 1]
reszta = 23

for nominal in nominaly:
    if nominal <= reszta:
        wydaj = reszta // nominal
        reszta = reszta % nominal
        print(f'{wydaj} x {nominal} zł')

print(reszta)