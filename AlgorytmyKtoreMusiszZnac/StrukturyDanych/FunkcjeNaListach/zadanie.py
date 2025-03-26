numbers = [1,45,672,7265,16] 

#last_num_sort = sorted(numbers, key=lambda x: int(str(x)[-1]))
last_num_sort = sorted(numbers, key=lambda x: x % 10) 
print(last_num_sort)

from functools import reduce

codes = ['JPID', 'JJJPPP', 'XXX', 'JDU'] 
max_code = len(reduce((lambda x,y: x if len(x) > len(y) else y), codes))
print(max_code)

capitals =['Rome', 'Paris', 'Madrid'] 
cities = ['Rome', 'Napoli', 'Rimini', 'Paris', 'Barcelona', 'Madrid', 'Marceille']

no_capitals = list(filter(lambda c: c not in capitals,  cities))
print(no_capitals)