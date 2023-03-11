N = int(input())
x = 0
i, j, k = (1,1,1)
AddJ , AddK = (0,0)

while(i <= N):

    if(i == N + 1): break
    
    print(i, j, k)
    
    if(x % 2 == 0):
        j += 1
        k += 1
        AddK += i
        pass
    else:
        i += 1  
        AddJ += 2
        j += AddJ
        k += AddK * 6
        pass
        
    x += 1
    x %= 2