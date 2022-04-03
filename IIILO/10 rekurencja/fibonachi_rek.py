def fib_iter(n):
    p1 = 1
    p2 = 1
    if n < 3: return p2
    
    for i in range(2, n):
        p1, p2 = p2, p1 + p2
    return p2
        

def fib_rek(n):
    if n < 3:
        return 1
    else:
        return fib_rek(n-1) + fib_rek(n-2)
    
n = 5
print(fib_rek(10))
print(fib_iter(10))