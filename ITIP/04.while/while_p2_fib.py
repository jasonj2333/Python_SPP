a, b = 0, 1
#a = 0
#b = 1

fib = [a, b]

while a<=400:
    a, b = b, a + b
    #a = b
    #b = a + b
    print(f"Aktualna wartość a = {a} i b = {b}")
    fib.append(b)
    
print(fib)