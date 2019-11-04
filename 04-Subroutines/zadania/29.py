import math

t = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
t.sort()

def mediana(t=t):
    if len(t)%2==0:
        print("A")
        a = t[int(len(t)/2)-1]
        b = t[(int(len(t)/2))]
        return (a+b)/2
    else:
        print("B")
        return t[math.floor(len(t)/2)]

def dominanta(t=t):
    a = {}
    for i in t: #first pass
        a.update({str(i):0})
    for i in t:
        a[str(i)] += 1
    return a

print(mediana())
print(dominanta())