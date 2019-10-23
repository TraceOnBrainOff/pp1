tab = [15, 8, 31, 47, 2, 19]
tabLen = len(tab)
revTab = []

for i in range(tabLen):
    currIndex = (tabLen-1)-i
    revTab.insert(i,tab[currIndex])
    
for i in revTab:
    print(i)