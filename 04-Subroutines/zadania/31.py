t = [2, 5, 4, 1, 8, 7, 4, 0, 9]
print(t)

def reverse(t):
    lt = []
    for i in range(len(t)):
        lt.append(t[len(t)-i-1])
    return lt

print(reverse(t))