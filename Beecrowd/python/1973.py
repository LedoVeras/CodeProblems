stars = int(input())

numbList = [int(x) for x in input().split(" ")]

total = sum(numbList)
stealed = 1
print(numbList)
curI = 0
i = 0
while True:
    cur = numbList[curI]
    dir = (cur % 2) * 2 - 1
    
    print(cur, curI, dir)

    curI += dir

    if(cur == 0 or curI < 0 or curI >= stars):
        break

    numbList[curI - dir] = cur - 1
    stealed += 1
    
    i += 1
    if i > 100:
        break
    
print(stealed, total - stealed)
