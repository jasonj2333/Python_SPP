#Kolejka FIFO
import queue
q = queue.Queue()

for i in range(11,16):
    q.put(i)
    
print(q.qsize())

print("--------------- Kolejka FIFO -----------------")

while q.qsize() > 0:
    print(f"Pobieram {q.get()}, pozostało elementów {q.qsize()}")
    
#Stos LIFO
lifo = queue.LifoQueue()

for i in range(21,26):
    lifo.put(i)

print(lifo.qsize())

print("--------------- STOS LIFO -----------------")
while lifo.qsize() > 0:
    print(f"Pobieram {lifo.get()}, pozostało elementów {lifo.qsize()}")

#Kolejka (FIFO) z prioretytami
priority_q = queue.PriorityQueue()
priority_q.put((1, "Zadanie o priorytecie 1"))
priority_q.put((3, "Zadanie o priorytecie 3"))
priority_q.put((2, "Zadanie o priorytecie 2"))
priority_q.put((2, "Zadanie o priorytecie 2 - ponownie"))

print("--------------- Kolejka FIFO z priorytetami -----------------")
while priority_q.qsize() > 0:
    print(f"Pobieram {priority_q.get()}, pozostało elementów {priority_q.qsize()}")