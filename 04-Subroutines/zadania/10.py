def f():
    y = x + 2 #5
    return x + y #8
x = 3
y = x + 4 #7
z = f() + x + y #8 + 3 + 7
print(x, y, z)