import time

# Algoritmi 1
def algo1(n):
    result = 0
    for i in range(n):
        result += i
    return result
# O(n)

# Algoritmi 2
def algo2(n):
    result = 0
    for i in range(n):
        result += i
    for i in range(n):
        result -= i
    return result
# O(n)

# Algoritmi 3
def algo3(n):
    return 5*n**2
# O(1)

# Algoritmi 4
def algo4(n):
    result = 0
    while n > 0:
        n -= 1
        result += 2
    return result
# O(n)

# Algoritmi 5
def algo5(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i*j
    return result
# O(n^2)

# Algoritmi 6
def algo6(n):
    result = 0
    for i in range(10):
        result += n
    return result
# O(1)

# Algoritmi 7
def algo7(n):
    result = n
    for i in range(100):
        for j in range(100):
            result -= 1
    return result
# O(1)

# Algoritmi 8
def algo8(n):
    return 1
    result = 0
    for i in range(n):
        result += 1
# O(1)
