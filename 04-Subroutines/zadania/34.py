def fib(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fibrec(R):
    R-=1
    if R==0:
        return 0,1
    else:
        a, b = fibrec(R)
        return b, a+b

print(fib(20))
print(fibrec(20)[0])