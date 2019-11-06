def check(t, num):
    d = {}
    for i in t: #definicja w dictionary
        d[str(i)] = 0
    for i in t:
        d[str(i)] += 1
    if d[str(num)] == 1:
        return True
    else:
        return False

def unikaty(t):
    s = []
    for i in t:
        if check(t, i) == True:
            s.append(i)
    return s

print(unikaty([1,1,2,2,3,3,4,4,5,6]))