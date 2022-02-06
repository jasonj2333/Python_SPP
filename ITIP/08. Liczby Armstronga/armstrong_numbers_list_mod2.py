import time

n = 8
start = 0
stop = 10 ** n

l_stop = len(str(stop))

power_list = []
power_list.append(-1)

def get_sum(number, n):
    sum_pow = 0
    while number > 0:
        digit = number % 10
        sum_pow += power_list[n][digit]
        number //= 10

    return sum_pow

def armstrong10(number):
    found_numbers = []
    n = len(str(number))
    temp = number//10
    sum_pow = get_sum(temp, n)

    if sum_pow % 2 == 0:

        for i in range(0, 10):
            result = sum_pow + power_list[n][i]
            if result == number + i:
                found_numbers.append(result)

    return found_numbers
            

start_time = time.time()
print(f"\n------- Wyszukiwanie liczb(y) Armstronga w przedziale {start} - {stop:_} ----------------------")
### Generowanie listy z wartościami n potęg wszystkich cyfr
for i in range(1, l_stop+1):
    ten_power_list = []
    for j in range(0,10):
        ten_power_list.append(j**i)

    power_list.append(ten_power_list)

## wyszukiwanie liczb Armstronga
armstrongs_list = []
for number in range(start, stop+1, 10):
    armstrongs_list.extend(armstrong10(number))
    

stop_time = time.time()
print(f"Znaleziono {len(armstrongs_list)} liczb Armstronga: {armstrongs_list} ")
print(f"W czasie: {stop_time-start_time}")


#### Na wyszukanie liczb Armstronga w przedziale 0 do 1 000 000 000 (metodą z listami) mój komputer potrzebował --- 221.11627960205078 seconds ---
#### znalezione w tym czasie liczby to:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474
# 54748
# 92727
# 93084
# 548834
# 1741725
# 4210818
# 9800817
# 9926315
# 24678050
# 24678051
# 88593477
# 146511208
# 472335975
# 534494836
# 912985153

#Łącznie 32