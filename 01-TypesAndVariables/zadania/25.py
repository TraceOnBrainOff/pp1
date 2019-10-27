a = "12103400001212905611117806"

b = ""
for i in range(2, len(a)):
    b += a[i]
    
result = a[0]+a[1]
for i in range(len(b)):
    if i%4==0:
        result += " " + b[i]
    else:
        result += b[i]
        
print(result)