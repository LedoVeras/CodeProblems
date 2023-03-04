def greater(a, b):
    return int((a + b + abs(a - b)) / 2)

numbList = input().split(" ")
  
curGreater = int(numbList[0])
for cur in numbList:
    curGreater = greater(curGreater, int(cur))

print(str(curGreater) + " eh o maior")