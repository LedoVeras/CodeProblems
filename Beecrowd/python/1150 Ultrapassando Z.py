n = int(input())

while True:
    cur = int(input())
    
    if(cur > n):
        
        j = 1
        su = n
        while su <= cur:
            su += n + j
            j += 1
        
        print(j)
        
        break