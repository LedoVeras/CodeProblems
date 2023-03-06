from decimal import *
getcontext().prec = 2
x = 0
i = Decimal(0)
j = 1
curJ = 7 

while(i <= 2):
    
    curJ = j + x

    if curJ % 1 == 0: curJ = int(curJ)
    
    priI = int(i) if i % 1 == 0 else str("%.1f" % i)
    
    print(f"I={priI} J={curJ}")
    
    if(x % 3 == 2):
        i += Decimal(0.2)
        j += Decimal(0.2)   
        
    x += 1
    x %= 3