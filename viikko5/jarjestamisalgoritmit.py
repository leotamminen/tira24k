import time
 
# Tätä funktiota käytetään lisäysjärjestämisessä
def swap(items, a, b):
    temp = items[a]
    items[a] = items[b]
    items[b] = temp
 
# Lisäysjärjestäminen (insertion sort) kurssin materiaalista
def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i - 1, -1, -1):
            if items[j] > items[j + 1]:
                swap(items, j, j + 1)
            else:
                break
 
# Lomitusjärjestäminen (merge sort) kurssin materiaalista
def merge_sort(items):
    n = len(items)
 
    if n == 1: return
 
    left = items[0:n//2]
    right = items[n//2:]
 
    merge_sort(left)
    merge_sort(right)
 
    a = b = 0
    for i in range(n):
        if b == len(right) or \
           (a < len(left) and left[a] < right[b]):
            items[i] = left[a]
            a += 1
        else:
            items[i] = right[b]
            b += 1
        
# Ajanotto
n = 10**5
syote1, syote2, syote3 = [list(range(1, n + 1))] * 3
 
# Lomitusjärjestäminen
aloitus = time.time()
tulos1 = merge_sort(syote1)
loppuaika = time.time()
print(f"Lomitusjärjestämisen suoritusaika: {loppuaika - aloitus} sekuntia")
 
# Lisäysjärjestäminen
aloitus = time.time()
tulos2 = insertion_sort(syote2)
loppuaika = time.time()
print(f"Lisäysjärjestämisen suoritusaika: {loppuaika - aloitus} sekuntia")
 
# Pythonin oma metodi sort
aloitus = time.time()
tulos3 = syote3.sort()
loppuaika = time.time()
print(f"Pythonin oman sort metodin suoritusaika: {loppuaika - aloitus} sekuntia")