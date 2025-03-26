l = [1,2,3]
#l

i = l.__iter__()
#i

print(i.__next__())
print(i.__next__())
print(i.__next__())

#i.__next__()

for n in l:
   print(n)

list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))

from functools import reduce

numbers = [11,22,33,1]

reduce(lambda x,y: x if x > y else y, numbers)

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(ids)


print(sorted(ids))

sorted_list = sorted(ids, key=lambda x: int(x[2:]))
print(sorted_list)

from heapq import nsmallest, nlargest

nlargest(3, ids, key=lambda x: int(x[2:]))
