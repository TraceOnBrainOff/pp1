a = "abc"
aNew = ""
for i in range(len(a)-1, -1, -1): #ok
    aNew = aNew + a[i]
    
print(aNew)