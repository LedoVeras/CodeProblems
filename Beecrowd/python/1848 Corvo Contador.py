caw = 0
nu = [0,0,0]
while True:
    cur = input()
    
    if cur == "caw caw":
        print(nu[caw])
        caw += 1
        if caw >= 3:break
        continue
        
    i = 3
    for s in cur:
        i -= 1
        if(s == "*"):
            nu[caw] = nu[caw] + 2 ** i