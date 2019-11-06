tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def suma(t):
    s = 0
    for i in t:
        if type(i) == int:
            s += i
        elif type(i) == list:
            s += suma(i)
    return s

print(suma(tab))