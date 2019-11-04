import random

def rzucKostka():
    res = random.randrange(1,6)
    print(res)
    return res

def sumujTablice(t):
    s = 0
    for i in t:
        s += i
    return s

t = []
for i in range(3):
    t.append(rzucKostka())

print(sumujTablice(t))