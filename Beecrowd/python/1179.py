pair = []
odd = []

for i in range(15):
    cur = int(input())
    if cur % 2 == 0:
        pair.append(cur)
    else:
        odd.append(cur)
        
    if(len(pair) == 5):
        for p in range(5):
            print(f"par[{p}] = {pair[p]}")
        pair.clear()
    elif(len(odd) == 5):
        for p in range(5):
            print(f"impar[{p}] = {odd[p]}")
        odd.clear()
        
for p in range(len(odd)):
    print(f"impar[{p}] = {odd[p]}")

for p in range(len(pair)):
    print(f"par[{p}] = {pair[p]}")