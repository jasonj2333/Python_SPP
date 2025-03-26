list_fifo = []

list_fifo.append("Plant a tree")
list_fifo.append("Build a house")
list_fifo.append("Have a son")

print(list_fifo)

while len(list_fifo) > 0:
   task = list_fifo.pop(0)
   print(task)

list_lifo = []

list_lifo.append('Blue Box with Glass')
list_lifo.append('Bag with Presents')
list_lifo.append('Barrel of Beer')
list_lifo.append('Cage with a Tiger')

print(list_lifo)

while len(list_lifo) > 0:
   task = list_lifo.pop()
   print(task)