import random
storage = [0,0,0,0,0,0]
nazwy = ["jedynka", "dwojka", "trojka", "czworka", "piatka", "szostka"]

for i in range(100):
    storage[random.randrange(6)] += 1

for i in range(len(storage)):
    print(nazwy[i], storage[i])