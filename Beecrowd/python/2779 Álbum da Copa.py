totfigs = int(input())
m = int(input())

numbList = []

for i in range(m):
    numbList.append(input())
    
numbList = set(numbList)

print(totfigs - len(numbList))