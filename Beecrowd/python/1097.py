x = 0
i = 1
j = 7
curJ = 7 

while(i <= 9):
    
    curJ = j - x
    
    print(f"I={i} J={curJ}")
    
    if(x % 3 == 2):
        i += 2
        j += 2   
        
    x += 1
    x %= 3