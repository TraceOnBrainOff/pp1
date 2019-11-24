import csv
data = []
keys = []
spaces = [4, 6, 8, 10]
with open('C:\\Users\\JUNK\\Desktop\\School\\pp1\\05-ModularProgramming\\zadania\\employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        keys = row.keys()
        data.append(row)

def displayHeader():
    order = [1,0,2,3]
    s = "#"+" "*spaces[0]
    for a in order:
        s+=keys[a]+" "*spaces[a]
    print(s)
    print("="*75)
displayHeader()
