import time
start = 0
stop = 10_000_000

def get_sum(number, n):
    sum_pow = 0
    while number > 0:
        digit = number % 10
        sum_pow += digit ** n
        number //= 10

    return sum_pow

def armstrong(number):
    n = len(str(number))
    sum_pow = get_sum(number, n)

    if sum_pow == number: return True

    return False

def armstrong10(number):
    n = len(str(number))
    temp  = number//10
    sum_pow = get_sum(temp, n)

    for i in range(0, 10):
        result = sum_pow + i ** n

        if result == number + i: print(result) 


start_time = time.time()

for number in range(start, stop+1, 10):
    armstrong10(number)

stop_time = time.time()
print(f"Time: {stop_time-start_time}")