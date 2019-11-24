import re
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

a = open(os.path.join(THIS_FOLDER, "land.txt"))
st = ""
for line in a:
    st += line

b = re.findall("(\d+[.,]\d+|\d\d+)", st)
s = 0
for i in b:
    s+=float(i.replace(",", "."))
print(s)