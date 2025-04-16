# 1. Dana jest ścieżka my_path='/home/boss/data/projects/bakery/prices.csv' 
# 2. Ponieważ właśnie poznaliśmy moduł queue… wyświetl poszczególne elementy tej ścieżki w odwrotnej kolejności: 
#     a. Pętlą for wpisz do odpowiedniej klasy z modułu queue wynik podziału ścieżki ze względu 
#     na znak slash (my_path.split(‘/’) 
#     b. Pętlą while wyświetl elementy z kolejki – najpierw powinno być wyświetlone prices.csv, 
#     potem bakery, potem projects itd. 
import queue

my_path='/home/boss/data/projects/bakery/prices.csv' 

lifo = queue.LifoQueue()

parts = my_path.split("/")
for part in parts:
    lifo.put(part)

while lifo.qsize() > 0:
    print(f"Pobieramm element {lifo.get()} pozostało {lifo.qsize()}")
