import re

st = "AcDc"

def whatev(s):
    a = re.findall('[A-Z]', s)
    b = ""
    for i in a:
        b+=i
    return b 

print(whatev(st))