numbList = input().split(" ")
A = int(numbList[0])
N = int(numbList[-1])
    
print(sum([A + i for i in range(N)]))