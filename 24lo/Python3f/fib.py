def fib(n):
    if(n < 3):
        return 1 #przypadek podstawowy
    else:
        return fib(n-1) + fib(n-2) #rekurencyjny
    
print( fib(13) )
    
