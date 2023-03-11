x = 0
i = 1
j = 7

while(i <= 9):
    
    j = 7 - x
    
    print(f"I={i} J={j}")
    
    if(x % 3 == 2):
        i += 2   
        
    x += 1
    x %= 3
    