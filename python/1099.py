n = int(input())

for i in range(n):
    numbList = input().split(" ")

    for i in range(len(numbList)):
        numbList[i] = int(numbList[i])

    A, B = numbList
    
    sum = 0
    for j in range(min(A , B) + 1 , max(A , B)):
        if(j % 2 == 1): sum += j
        
    print(sum)