rok = int(input())

if rok % 4 == 0 and rok % 100 != 0:
  print(f"Rok {rok} jest przestępny")
elif rok % 400 == 0:
  print(f"Rok {rok} jest przestępny")
else:
  print(f"Rok {rok} nie jest przestępny")