N = int(input())

for i in range(N):
    numbList = input().split(" ")

    for i in range(len(numbList)):
      numbList[i] = int(numbList[i])

    X, Y = numbList

    sum = 0
    start = (X + 1) if (X % 2 == 0) else (X)
    
    for j in range(Y):
        sum += start + j * 2
    
    print(sum)