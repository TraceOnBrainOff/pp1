#Basic arithmetic b, f, h
print("\nBasic Arithmetic:::")
a = [5, 1, 8, 6, 3]
b = 0
c = 0
for n in a:
    b = b + n*n
    
for n in a:
    c = c + n
    
print(c) #a

print(b) #b 

print(a[2]/a[4]) #c

print(a[0]%a[4]) #d

print((a[0]+a[1])/(a[3]+a[4]))#e

print(a[0]%3) #f

print(a[2]==a[3])#g

print(a[2]>>4) #h