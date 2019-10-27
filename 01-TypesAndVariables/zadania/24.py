import math
ratio = 0.393700787
wys = 170
cale = wys*ratio
a = math.floor((cale/12-math.floor(cale/12))*10)
b = math.floor(cale/12)
print("Mam {} cm wzrostu, tj. {} stóp i {} cali.".format(wys, b, a))