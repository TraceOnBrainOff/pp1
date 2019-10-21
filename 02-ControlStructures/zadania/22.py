a = [15, 8, 31, 47, 2, 19]
suma = 0
n = 0

for e in a:
    if e%2!=0:
        n+=1
        suma = suma + e
    
x = suma/n
print(x)