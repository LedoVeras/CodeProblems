n = int(input())

for i in range(n):
    j = int(input())
    
    su = 0
    
    for l in range(1 , j):
        if(j % l == 0):
            su += l 
            
    print(j, "" if su == j else " nao", " eh perfeito", sep="")