import random
class Dice:
    def __init__(self):
        self.v = random.randrange(1,6)
    def r(self):
        print(self.v)
        return self.v

a = []
for i in range(3):
    b = Dice()
    b.r()
    a.append(b)

    