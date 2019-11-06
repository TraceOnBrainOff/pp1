f = lambda x: x%2==0
t = [1,2,3,4,5,6,7,8,9]
a = filter(f, t) #dziwne że nie można printować tego obiektu

for i in a:
    print(i)