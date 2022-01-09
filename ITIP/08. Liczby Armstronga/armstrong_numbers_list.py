import time


start = 0
stop = 100_000_000

l_stop = len(str(stop))

power_list = []
power_list.append(-1)

def get_sum(number, n):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += power_list[n][digit]
        number //= 10

    return sum

def armstrong(number):
    n = len(str(number))
    sum = get_sum(number, n)

    if number == sum: return True

    return False

def armstrong10(number):
    n = len(str(number))
    temp = number//10
    sum = get_sum(temp, n)

    for i in range(0, 10):
        result = sum + power_list[n][i]
        if result == number + i:
            print(result)

start_time = time.time()

# for number in range(start, stop+1, 10):
#     armstrong10(number)

for i in range(1, l_stop+1):
    #power_list.append(i)

    ten_power_list = []
    for j in range(0,10):
        ten_power_list.append(j**i)

    power_list.append(ten_power_list)

print(power_list)

for number in range(start, stop+1, 10):
    armstrong10(number)

stop_time = time.time()
print(f"Time: {stop_time-start_time}")