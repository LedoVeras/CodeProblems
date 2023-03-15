f, s, g, u, d = [int(x) for x in input().split(" ")]

i = 0

while True:
    prevS = s
    
    dir = (s - g)
    if(dir < 0):
        s += u
    elif(dir > 0):
        s += -d
    else:
        break
    print(s, dir)
    i += 1
    
    if(i > 1000 or prevS == s):
        break
    
print(i)