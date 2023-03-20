n = int(input())

for i in range(n):
    j = int(input())
    
    prime = True
    
    for l in range(2 , j):
        if(j % l == 0):
            prime = False
            break
            
    print(j, "" if prime else " nao", " eh primo", sep="")