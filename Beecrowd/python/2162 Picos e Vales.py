def sign(i):
    dif = numbList[i + 1] - numbList[i]
    return 0 if dif == 0 else (1 if dif > 0 else -1)

n = int(input())
numbList = [int(x) for x in input().split(" ")]

result = 1

cur = sign(0)
if(cur == 0):
    result = 0
else:
    for i in range(1, n - 1):
        c = sign(i)
        
        if(c == 0 or c == cur):
            result = 0
            break
        
        cur = c

print(result)
