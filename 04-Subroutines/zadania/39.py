x = 3
y = 7
#zakres <x,y>

def clamp(x,y,z):
    if not x<=y:
        print("Invalid parameter sizes")
        return False
    if z < x:
        return False
    if z > y:
        return False
    if x<=z<=y:
        return True

print(clamp(x,y,5))