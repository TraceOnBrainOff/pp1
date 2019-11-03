import re

s = "wtorek - 23C, środa - 21C, czwartek 25C"
c = re.findall("\d{2}",s)
a = 0
for b in c:
    a += int(b)

print(a/len(c))