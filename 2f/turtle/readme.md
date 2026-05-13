# 🐢 Turtle — Ściąga Python (`from turtle import *`)

## 📦 Import modułu

```python id="t1"
from turtle import *
```

---

# 🎯 Ruch żółwia

| Polecenie     | Skrót     | Opis           |
| ------------- | --------- | -------------- |
| `forward(x)`  | `fd(x)`   | ruch do przodu |
| `backward(x)` | `bk(x)`   | ruch do tyłu   |
| `left(kąt)`   | `lt(kąt)` | obrót w lewo   |
| `right(kąt)`  | `rt(kąt)` | obrót w prawo  |

### Przykład

```python id="t2"
fd(100)
lt(90)
```

---

# ✏️ Pisak

| Polecenie   | Skrót  | Opis                |
| ----------- | ------ | ------------------- |
| `penup()`   | `pu()` | podniesienie pisaka |
| `pendown()` | `pd()` | opuszczenie pisaka  |

### Przykład

```python id="t3"
pu()
goto(100,100)
pd()
```

---

# 🎨 Kolory i styl

| Polecenie          | Opis            |
| ------------------ | --------------- |
| `color("red")`     | kolor linii     |
| `bgcolor("black")` | kolor tła       |
| `pensize(3)`       | grubość linii   |
| `speed(10)`        | szybkość żółwia |

### Przykład

```python id="t4"
color("blue")
pensize(5)
```

---

# 📍 Pozycja

| Polecenie         | Opis                |
| ----------------- | ------------------- |
| `goto(x,y)`       | przejście do punktu |
| `position()`      | aktualna pozycja    |
| `setheading(kąt)` | ustawienie kierunku |

---

# 🧭 Układ współrzędnych

```text
       y+
        ↑
x- ← (0,0) → x+
        ↓
       y-
```

---

# 🔷 Pętle

## Kwadrat

```python id="t5"
for i in range(4):
    fd(100)
    lt(90)
```

---

## Trójkąt

```python id="t6"
for i in range(3):
    fd(100)
    lt(120)
```

---

## Sześciokąt

```python id="t7"
for i in range(6):
    fd(100)
    lt(60)
```

---

# 🎨 Wypełnianie figur

```python id="t8"
begin_fill()

for i in range(4):
    fd(100)
    lt(90)

end_fill()
```

---

# ⭐ Najważniejsze kąty

| Figura     | Kąt obrotu |
| ---------- | ---------- |
| trójkąt    | 120°       |
| kwadrat    | 90°        |
| pięciokąt  | 72°        |
| sześciokąt | 60°        |

## Wzór

```python id="t9"
kąt = 360 / liczba_boków
```

---

# ⏱️ Szybkość żółwia

```python id="t10"
speed(1)    # wolno
speed(10)   # szybko
speed(0)    # najszybciej
```

---

# 🛑 Zakończenie programu

```python id="t11"
done()
```

👉 pozostawia okno otwarte

---

# 🧪 Pełny przykład

```python id="t12"
from turtle import *

speed(10)
color("green")
pensize(3)

for i in range(4):
    fd(100)
    lt(90)

done()
```
