import math
kwota = 48
monety = [0,0,0] #5,2,1

if kwota>=5:
    a = math.floor(kwota/5)
    kwota -= a*5
    monety[0] = a

if kwota>=2:
    a = math.floor(kwota/2)
    kwota -= a*2
    monety[1] = a
    
if kwota>=1:
    a = math.floor(kwota/1)
    kwota -= a*1
    monety[2] = a