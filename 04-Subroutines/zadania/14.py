l = 23
t = [15,38,7,23,14]
def sprawdzLiczbe(l, t):
    for i in t:
        if l==i:
            print("Występuje")
            return
    print("Nie występuje")

sprawdzLiczbe(l, t)

