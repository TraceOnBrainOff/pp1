a = 5

for i in range(a):
    b = ""
    for j in range(i):
        b = b + "*"
    print(b)

for i in range(a):
    b = ""
    for j in range(a-i):
        b = b + "*"
    print(b)