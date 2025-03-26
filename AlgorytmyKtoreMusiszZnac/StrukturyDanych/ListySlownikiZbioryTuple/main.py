print(range(10))

print(list(range(10, 0, -1)))

t1 = (1,2)
print(t1)

t1[1]

t2 = (1, 2, 'green', ['Berlin','Warsaw','Paris'])
print(t2)

t2[3][2]

(*t2, 99)

(t2 + (99,))

healthy = {'vegetables', 'bread', 'milk', 'eggs'}

drinks = {'beer', 'caffe', 'tea', 'milk'}

print('milk' in drinks)

print('chips' in healthy)

print(healthy | drinks)

print(healthy & drinks)

pricelist = {
'milk' : 2,
'bread': 4,
'butter': 3
}

print(pricelist)

for k,v in pricelist.items():
   print(k, v)

for k in pricelist.keys():
   print(k, pricelist[k])

print(pricelist['bread'])