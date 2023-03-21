import re
s = input().strip()

t = re.compile(r'[a-z]|[A-Z]')
l = t.findall(s)
if(len(l)>1):
    s = s[:s.index(l[0])]
print(s[::-1])

